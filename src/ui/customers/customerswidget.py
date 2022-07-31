from PySide6.QtWidgets import QWidget, QHeaderView, QMessageBox, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QModelIndex, QSize

from .customerswidget_ui import CustomersWidget_UI
from .customerdialog import CustomerDialog

from core.user import User
from core.customers.customers_model import CustomersModel

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

    def add(self) -> None:
        customer_dialog = CustomerDialog(self.user)
        customer_dialog.exec()

        if customer_dialog.model_needs_update():
            self.model.fetch_data()

    def edit(self) -> None:
        selection = self.customers_tableview.selectionModel()
        if not selection.hasSelection():
            self.model_loaded()
            
            message_box = QMessageBox()
            message_box.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText(self.tr('Select the customer to modify and try again.'))

            accept_button = QPushButton(QIcon('qrc/icons/ok.png'), self.tr('Accept'), message_box)
            accept_button.setIconSize(QSize(32, 32))
            message_box.addButton(accept_button, QMessageBox.AcceptRole)

            message_box.exec()
            return

        customer = self.model.customer_from_index(selection.currentIndex())
        customer_dialog = CustomerDialog(self.user)
        customer_dialog.set_customer(customer)
        customer_dialog.exec()

        if customer_dialog.model_needs_update():
            self.model.fetch_data()

    def model_loaded(self) -> None:
        selection = self.customers_tableview.selectionModel()
        if not selection.hasSelection():
            self.edit_button.setEnabled(False)
            self.delete_button.setEnabled(False)

    def customer_clicked(self, index: QModelIndex) -> None:
        if index.isValid():
            self.edit_button.setEnabled(True)
            self.delete_button.setEnabled(True)