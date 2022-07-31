from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import Qt, QTimer

from network.jsonjob import JsonJob

from .customerdialog_ui import CustomerDialog_UI

from core.customers.customer import Customer
from core.user import User
from core.enums import MessageType

class CustomerDialog(CustomerDialog_UI, QDialog):
    def __init__(self, user: User, parent: QWidget = None) -> None:
        super(CustomerDialog, self).__init__(parent)
        self.setup(user)

    def setup(self, user: User) -> None:
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle(self.tr('Customer'))
        self.setModal(True)

        self.hide_notifications()

        self.accept_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.reject)

        self.customer = None
        self.user = user

        self.needs_update = False

    def set_customer(self, customer: Customer) -> None:
        self.customer = customer

        if customer:
            self.name_lineedit.setText(customer.name)
            self.phone_lineedit.setText(customer.phone)
            self.email_lineedit.setText(customer.email)
            self.address_textedit.setPlainText(customer.address)

    def accept_clicked(self) -> None:
        name = self.name_lineedit.text().strip()
        if not name:
            self.show_notification('Enter a name and try again.', MessageType.Error)
            return

        customer = Customer()
        customer.name = name
        customer.phone = self.phone_lineedit.text().strip()
        customer.email = self.email_lineedit.text().strip()
        customer.address = self.address_textedit.toPlainText().strip()

        if self.customer:
            customer.id = self.customer.id
            job = JsonJob(f'/customers/{customer.id}', self.user, 'PUT')
        else:
            job = JsonJob('/customers', self.user, 'POST')
            
        job.finished.connect(self.job_finished)
        job.set_body(customer.to_json())
        job.start()

    def job_finished(self, data: dict) -> None:
        if not data:
            self.show_notification('An error ocurred, try again.', MessageType.Error)
            return

        status_code = data['response_status']['status']

        if status_code != 200:
            self.show_notification(data['response_status']['message'], MessageType.Error)
            return

        self.needs_update = True
        if not self.keeppen_checkbox.isChecked():
            self.accept()
        else:
            self.show_notification(data['response_status']['message'])
            self.clear_fields()

            if self.customer:
                self.customer = None

    def show_notification(self, message: str, type: MessageType = MessageType.Information) -> None:
        self.setFixedHeight(405)

        if type == MessageType.Information:
            self.toast_success_label.setText(message)
            self.toast_success_label.setVisible(True)
        elif type == MessageType.Error:
            self.toast_error_label.setText(message)
            self.toast_error_label.setVisible(True)

        QTimer.singleShot(3000, self.hide_notifications)

    def hide_notifications(self) -> None:
        self.toast_success_label.hide()
        self.toast_error_label.hide()
        self.setFixedHeight(357)

    def clear_fields(self):
        self.name_lineedit.clear()
        self.phone_lineedit.clear()
        self.email_lineedit.clear()
        self.address_textedit.clear()
        self.name_lineedit.setFocus()

    def model_needs_update(self):
        return self.needs_update