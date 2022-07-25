from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

from .brookesiapos_ui import BrookesiaPOS_UI
from ui.sales.saleswidget import SalesWidget

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

        self.action_minimize.triggered.connect(self.showMinimized)
        self.action_exit.triggered.connect(QApplication.instance().quit)

        self.user = user

        with open('qrc/theme/default/mainwindow.qss', 'r') as qss:
            theme = qss.read()
        
        if theme:
            self.setStyleSheet(theme)

        self.views = {}
        
        self.load_salesview()

    def load_salesview(self):
        salesview = SalesWidget(self)
        self.views_stackedwidget.addWidget(salesview)
        self.views['salesview'] = 0