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

        self.action_sales.triggered.connect(lambda: self.views_stackedwidget.setCurrentIndex(self.views.get('salesview')))
        self.action_customers.triggered.connect(lambda: self.views_stackedwidget.setCurrentIndex(self.views.get('customersview')))
        self.action_products.triggered.connect(lambda: self.views_stackedwidget.setCurrentIndex(self.views.get('productsview')))

        self.action_about.triggered.connect(self.about)
        self.action_minimize.triggered.connect(self.showMinimized)
        self.action_exit.triggered.connect(QApplication.instance().quit)

        self.user = user

        with open('qrc/theme/default/mainwindow.qss', 'r') as qss:
            theme = qss.read()
        
        if theme:
            self.setStyleSheet(theme)

        self.views = {}
        
        self.load_salesview()
        self.load_customersview()
        self.load_productsview()

    def load_salesview(self) -> None:
        salesview = SalesWidget(self)
        self.views_stackedwidget.addWidget(salesview)
        self.views['salesview'] = 0

    def load_customersview(self) -> None:
        customersview = CustomersWidget(self)
        self.views_stackedwidget.addWidget(customersview)
        self.views['customersview'] = 1

    def load_productsview(self) -> None:
        productsview = ProductsWidget(self)
        self.views_stackedwidget.addWidget(productsview)
        self.views['productsview'] = 2

    def about(self) -> None:
        about = AboutDialog(None)
        #about.setWindowModality(Qt.ApplicationModal)
        about.exec()