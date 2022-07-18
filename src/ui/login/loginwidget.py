import os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from .loginwidget_ui import Ui_loginwidget

class LoginWidget(Ui_loginwidget, QWidget):
    def __init__(self):
        super(LoginWidget, self).__init__()
        self.setup()

    def setup(self):
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle(self.tr('Brookesia POS Login'))

        self.login_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(self.exit)

    def login(self):
        pass

    def exit(self):
        QApplication.instance().quit()