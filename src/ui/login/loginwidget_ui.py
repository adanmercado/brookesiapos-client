# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class LoginWidget_UI(object):
    def setupUi(self, loginwidget):
        if not loginwidget.objectName():
            loginwidget.setObjectName(u"loginwidget")
        loginwidget.resize(300, 170)
        loginwidget.setMinimumSize(QSize(300, 170))
        self.verticalLayout = QVBoxLayout(loginwidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.username_lineedit = QLineEdit(loginwidget)
        self.username_lineedit.setObjectName(u"username_lineedit")
        self.username_lineedit.setMinimumSize(QSize(0, 45))

        self.verticalLayout.addWidget(self.username_lineedit)

        self.password_lineedit = QLineEdit(loginwidget)
        self.password_lineedit.setObjectName(u"password_lineedit")
        self.password_lineedit.setMinimumSize(QSize(0, 45))
        self.password_lineedit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_lineedit)

        self.toast_error_label = QLabel(loginwidget)
        self.toast_error_label.setObjectName(u"toast_error_label")
        self.toast_error_label.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.toast_error_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.login_button = QPushButton(loginwidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(0, 45))
        icon = QIcon()
        icon.addFile(u"qrc/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.login_button)

        self.exit_button = QPushButton(loginwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(0, 45))
        icon1 = QIcon()
        icon1.addFile(u"qrc/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.exit_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(loginwidget)

        QMetaObject.connectSlotsByName(loginwidget)
    # setupUi

    def retranslateUi(self, loginwidget):
        loginwidget.setWindowTitle("")
        self.username_lineedit.setPlaceholderText(QCoreApplication.translate("loginwidget", u"Username", None))
        self.password_lineedit.setPlaceholderText(QCoreApplication.translate("loginwidget", u"Password", None))
        self.toast_error_label.setText("")
        self.login_button.setText(QCoreApplication.translate("loginwidget", u"Login", None))
        self.exit_button.setText(QCoreApplication.translate("loginwidget", u"Exit", None))
    # retranslateUi

