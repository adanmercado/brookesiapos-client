from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

from .brookesiapos_ui import BrookesiaPOS_UI
from ui.sales.saleswidget import SalesWidget
from ui.customers.customerswidget import CustomersWidget
from ui.products.productswidget import ProductsWidget

from ui.about.aboutdialog import AboutDialog

from core.user import User

class BrookesiaPOS(BrookesiaPOS_UI, QMainWindow):
    def __init__(self, user: User) -> None:
        super(BrookesiaPOS, self).__init__()
        self.setup(user)

    def setup(self, user: User) -> None:
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle(self.tr('Brookesia POS'))

        self.action_sales.triggered.connect(self.change_view)
        self.action_customers.triggered.connect(self.change_view)
        self.action_products.triggered.connect(self.change_view)

        self.user = user

        self.action_about.triggered.connect(self.about)
        self.action_minimize.triggered.connect(self.showMinimized)
        self.action_exit.triggered.connect(QApplication.instance().quit)

        with open('qrc/theme/default/mainwindow.qss', 'r') as qss:
            theme = qss.read()
        
        if theme:
            self.setStyleSheet(theme)

        self.views = {}
        
        self.load_salesview()
        self.load_customersview()
        self.load_productsview()

        self.current_view = self.action_sales
        self.current_view.setDisabled(True)

    def load_salesview(self) -> None:
        salesview = SalesWidget(self)
        self.views_stackedwidget.addWidget(salesview)
        self.views['action_sales'] = 0

    def load_customersview(self) -> None:
        customersview = CustomersWidget(self.user, self)
        self.views_stackedwidget.addWidget(customersview)
        self.views['action_customers'] = 1

    def load_productsview(self) -> None:
        productsview = ProductsWidget(self)
        self.views_stackedwidget.addWidget(productsview)
        self.views['action_products'] = 2

    def change_view(self) -> None:
        sender_name = self.sender().objectName()
        index = self.views.get(sender_name, None)

        if index != None:
            if self.current_view:
                self.current_view.setEnabled(True)
            
            self.current_view = self.sender()
            self.current_view.setDisabled(True)
            
            self.views_stackedwidget.setCurrentIndex(index)

    def about(self) -> None:
        about = AboutDialog(None)
        about.exec()