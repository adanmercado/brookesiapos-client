from hashlib import sha256
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt, QTimer

from .loginwidget_ui import Ui_loginwidget
from network.jsonjob import JsonJob

class LoginWidget(Ui_loginwidget, QWidget):
    def __init__(self):
        super(LoginWidget, self).__init__()
        self.setup()

    def setup(self):
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle(self.tr('Brookesia POS Login'))
        self.setFixedSize(300, 170)

        self.login_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(self.exit)

        self.error_label.setVisible(False)

    def login(self):
        username = self.username_lineedit.text().strip()
        if not username:
            self.show_error('Enter a username and try again.')
            return
        
        password = self.password_lineedit.text().strip()
        if not password:
            self.show_error('Enter a password and try again.')
            return

        password = sha256(password.encode()).hexdigest()

        job = JsonJob('/users/auth', method='POST')
        job.finished.connect(self.validate_user)

        data = {
            'username': username,
            'password': password
        }
        job.set_body(data)

        job.start()

    def validate_user(self, data: dict):
        status_code = data['response_status']['status']

        if status_code == 200 and data['data']:
            print('Auth ok')
        elif status_code == 201:
            self.show_error(self.tr('Bad password'))
        elif status_code == 404:
            self.show_error(self.tr('User not found'))
        else:
            self.show_error(data['response_status']['message'])

    def exit(self):
        QApplication.instance().quit()

    def show_error(self, message):
        self.error_label.setText(message)
        self.setFixedHeight(210)
        self.error_label.setVisible(True)

        QTimer.singleShot(3000, self.hide_error)

    def hide_error(self):
        self.error_label.setVisible(False)
        self.setFixedHeight(170)