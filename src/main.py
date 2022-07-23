import sys

from PySide6.QtCore import QCoreApplication, Qt

from application import Application

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = Application(sys.argv)
    app.show_login()
    sys.exit(app.exec())