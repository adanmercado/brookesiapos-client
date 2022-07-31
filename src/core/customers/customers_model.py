from typing import Any

from PySide6.QtCore import QAbstractTableModel, QObject, QModelIndex, Qt, Signal

from network.jsonjob import JsonJob

from core.user import User
from core.customers.customer import Customer

class CustomersModel(QAbstractTableModel):
    data_fetched = Signal()

    def __init__(self, user: User, parent: QObject) -> None:
        super().__init__(parent)
        self.setup(user)

    def setup(self, user: User) -> None:
        self.user = user
        self.customers = []
        self.headers = ['Id', self.tr('Name'), self.tr('Address'), self.tr('Phone'), self.tr('Email')]

        #self.fetch_data()

    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.customers)

    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any:
        if role == Qt.DisplayRole:
            customer = self.customers[index.row()]

            if index.column() == 0:
                return customer.id
            elif index.column() == 1:
                return customer.name
            elif index.column() == 2:
                return customer.address
            elif index.column() == 3:
                return customer.phone
            elif index.column() == 4:
                return customer.email

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def fetch_data(self) -> None:
        job = JsonJob('/customers', self.user)
        job.finished.connect(self.load_data)
        job.start()

    def load_data(self, data: dict) -> None:
        if not data:
            print('CustomersModel: Invalid data')
            return

        status_code = data['response_status']['status']

        if status_code != 200:
            self.show_error(data['response_status']['message'])
            return
        
        customers_list = data['data']
        new_customers = []
        for customer in customers_list:
            item = Customer.from_json(customer)
            new_customers.append(item)

        if self.customers:
            self.beginResetModel()
            self.customers = []
            self.endResetModel()

        if new_customers:
            self.beginInsertRows(QModelIndex(), 0, len(new_customers) - 1)
            self.customers = new_customers
            self.endInsertRows()

        self.data_fetched.emit()

    def customer_from_index(self, index: QModelIndex) -> Customer:
        if index.isValid():
            return self.customers[index.row()]
        return Customer()