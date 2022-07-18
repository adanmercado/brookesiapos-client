import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import Qt

from ui.login.loginwidget import LoginWidget

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    app.setApplicationName('Brookesia POS')
    app.setApplicationDisplayName('Brookesia POS')
    app.setApplicationVersion('1.0.0')
    app.setOrganizationName('adanmercado')
    app.setOrganizationDomain('adanmercado.brookesiapos')

    login = LoginWidget()
    login.show()

    sys.exit(app.exec())