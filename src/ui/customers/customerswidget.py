from PySide6.QtWidgets import QWidget, QHeaderView

from .customerswidget_ui import CustomersWidget_UI

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
        self.customers_tableview.setModel(self.model)

        self.customers_tableview.hideColumn(0)
        self.customers_tableview.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.customers_tableview.setShowGrid(True)