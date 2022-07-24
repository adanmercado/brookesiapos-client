from hashlib import sha256

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QTimer, Signal

from .loginwidget_ui import Ui_loginwidget

from core.user import User
from network.jsonjob import JsonJob

class LoginWidget(Ui_loginwidget, QWidget):
    logged_in = Signal(User)

    def __init__(self) -> None:
        super(LoginWidget, self).__init__()
        self.setup()

    def setup(self) -> None:
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.tr('Brookesia POS Login'))
        self.setFixedSize(300, 170)

        self.login_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(QApplication.instance().quit)

        self.error_label.setVisible(False)

        with open('qrc/theme/default/login.qss') as qss:
            theme = qss.read()

        if theme:
            self.setStyleSheet(theme)

    def login(self) -> None:
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

    def validate_user(self, data: dict) -> None:
        status_code = data['response_status']['status']

        if status_code == 200 and data['data']:
            user = User.from_json(data['data'][0])
            self.logged_in.emit(user)
            self.close()
        elif status_code == 201:
            self.show_error(self.tr('Bad password'))
        elif status_code == 404:
            self.show_error(self.tr('User not found'))
        else:
            self.show_error(data['response_status']['message'])

    def show_error(self, message: str) -> None:
        self.error_label.setText(message)
        self.setFixedHeight(210)
        self.error_label.setVisible(True)

        QTimer.singleShot(3000, self.hide_error)

    def hide_error(self) -> None:
        self.error_label.setVisible(False)
        self.setFixedHeight(170)