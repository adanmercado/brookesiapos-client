from PySide6.QtWidgets import QApplication

from ui.login.loginwidget import LoginWidget

class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
        self.setup()

    def setup(self):
        self.setApplicationName('Brookesia POS')
        self.setApplicationDisplayName('Brookesia POS')
        self.setApplicationVersion('1.0.0')
        self.setOrganizationName('adanmercado')
        self.setOrganizationDomain('adanmercado.brookesiapos')

        with open('qrc/theme/default/brookesia.qss', 'r') as qss:
            theme = qss.read()
    
        if theme:
            self.setStyleSheet(theme)

    def show_login(self):
        self.login = LoginWidget()
        self.login.show()

    def show_brookesiapos(self):
        pass