from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtCore import QModelIndex

from .customerswidget_ui import CustomersWidget_UI
from .customerdialog import CustomerDialog
from ui.messagebox.messagebox import MessageBox

from core.user import User
from core.customers.customers_model import CustomersModel
from network.jsonjob import JsonJob

class CustomersWidget(CustomersWidget_UI, QWidget):
    def __init__(self, user: User, parent: QWidget) -> None:
        super(CustomersWidget, self).__init__(parent)
        self.setup(user)

    def setup(self, user: User) -> None:
        self.setupUi(self)

        self.user = user

        self.model = CustomersModel(self.user, self)
        self.model.data_fetched.connect(self.model_loaded)
        self.customers_tableview.setModel(self.model)
        self.model.fetch_data()

        self.customers_tableview.hideColumn(0)
        self.customers_tableview.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.customers_tableview.setShowGrid(True)
        self.customers_tableview.clicked.connect(self.customer_clicked)

        self.add_button.clicked.connect(self.add)
        self.edit_button.clicked.connect(self.edit)
        self.delete_button.clicked.connect(self.delete)

    def add(self) -> None:
        customer_dialog = CustomerDialog(self.user)
        customer_dialog.exec()

        if customer_dialog.model_needs_update():
            self.model.fetch_data()

    def edit(self) -> None:
        selection = self.customers_tableview.selectionModel()
        if not selection.hasSelection():
            self.model_loaded()
            MessageBox(MessageBox.Warning, self.tr('Select the customer to modify and try again.')).exec()
            return

        customer = self.model.customer_from_index(selection.currentIndex())
        customer_dialog = CustomerDialog(self.user)
        customer_dialog.set_customer(customer)
        customer_dialog.exec()

        if customer_dialog.model_needs_update():
            self.model.fetch_data()

    def delete(self) -> None:
        selection = self.customers_tableview.selectionModel()
        if not selection.hasSelection():
            self.model_loaded()
            MessageBox(MessageBox.Warning, self.tr('Select the customer to delete and try again.')).exec()
            return

        if MessageBox(MessageBox.Question, 'Are you sure you want to delete selected customer?').exec() == MessageBox.RejectRole:
            return

        
        customer = self.model.customer_from_index(selection.currentIndex())
        job = JsonJob(f'/customers/{customer.id}', self.user, method='DELETE')
        job.finished.connect(self.customer_deleted)
        job.finished_with_error.connect(lambda message: MessageBox(MessageBox.Critical, message).exec())
        job.start()

    def model_loaded(self) -> None:
        selection = self.customers_tableview.selectionModel()
        if not selection.hasSelection():
            self.edit_button.setEnabled(False)
            self.delete_button.setEnabled(False)

    def customer_clicked(self, index: QModelIndex) -> None:
        if index.isValid():
            self.edit_button.setEnabled(True)
            self.delete_button.setEnabled(True)

    def customer_deleted(self, data: dict):
        status_code = data['response_status']['status']

        if status_code != 200:
            MessageBox(MessageBox.Critical, data['response_status']['message']).exec()
            return

        self.model.fetch_data()