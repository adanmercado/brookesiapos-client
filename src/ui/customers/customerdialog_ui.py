# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customerdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class CustomerDialog_UI(object):
    def setupUi(self, customerdialog):
        if not customerdialog.objectName():
            customerdialog.setObjectName(u"customerdialog")
        customerdialog.resize(400, 357)
        customerdialog.setMinimumSize(QSize(400, 357))
        customerdialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(customerdialog)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.phone_lineedit = QLineEdit(customerdialog)
        self.phone_lineedit.setObjectName(u"phone_lineedit")
        self.phone_lineedit.setMinimumSize(QSize(0, 45))
        self.phone_lineedit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.phone_lineedit, 1, 1, 1, 1)

        self.phone_label = QLabel(customerdialog)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(0, 45))
        self.phone_label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.phone_label, 1, 0, 1, 1)

        self.address_textedit = QPlainTextEdit(customerdialog)
        self.address_textedit.setObjectName(u"address_textedit")
        self.address_textedit.setMinimumSize(QSize(0, 90))
        self.address_textedit.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.address_textedit, 3, 1, 1, 1)

        self.email_lineedit = QLineEdit(customerdialog)
        self.email_lineedit.setObjectName(u"email_lineedit")
        self.email_lineedit.setMinimumSize(QSize(0, 45))
        self.email_lineedit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.email_lineedit, 2, 1, 1, 1)

        self.name_lineedit = QLineEdit(customerdialog)
        self.name_lineedit.setObjectName(u"name_lineedit")
        self.name_lineedit.setMinimumSize(QSize(0, 45))
        self.name_lineedit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.name_lineedit, 0, 1, 1, 1)

        self.name_label = QLabel(customerdialog)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(0, 45))
        self.name_label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.email_label = QLabel(customerdialog)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMinimumSize(QSize(0, 45))
        self.email_label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)

        self.address_label = QLabel(customerdialog)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(0, 64))

        self.gridLayout.addWidget(self.address_label, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.keeppen_checkbox = QCheckBox(customerdialog)
        self.keeppen_checkbox.setObjectName(u"keeppen_checkbox")
        self.keeppen_checkbox.setMinimumSize(QSize(0, 36))

        self.verticalLayout.addWidget(self.keeppen_checkbox)

        self.toast_success_label = QLabel(customerdialog)
        self.toast_success_label.setObjectName(u"toast_success_label")
        self.toast_success_label.setMinimumSize(QSize(0, 40))
        self.toast_success_label.setTextFormat(Qt.PlainText)
        self.toast_success_label.setScaledContents(True)
        self.toast_success_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.toast_success_label)

        self.toast_error_label = QLabel(customerdialog)
        self.toast_error_label.setObjectName(u"toast_error_label")
        self.toast_error_label.setMinimumSize(QSize(0, 40))
        self.toast_error_label.setTextFormat(Qt.PlainText)
        self.toast_error_label.setScaledContents(True)
        self.toast_error_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.toast_error_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.accept_button = QPushButton(customerdialog)
        self.accept_button.setObjectName(u"accept_button")
        self.accept_button.setMinimumSize(QSize(0, 45))
        icon = QIcon()
        icon.addFile(u"qrc/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accept_button.setIcon(icon)
        self.accept_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.accept_button)

        self.cancel_button = QPushButton(customerdialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 45))
        icon1 = QIcon()
        icon1.addFile(u"qrc/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_button.setIcon(icon1)
        self.cancel_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.cancel_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.name_lineedit, self.phone_lineedit)
        QWidget.setTabOrder(self.phone_lineedit, self.email_lineedit)
        QWidget.setTabOrder(self.email_lineedit, self.address_textedit)
        QWidget.setTabOrder(self.address_textedit, self.keeppen_checkbox)
        QWidget.setTabOrder(self.keeppen_checkbox, self.accept_button)
        QWidget.setTabOrder(self.accept_button, self.cancel_button)

        self.retranslateUi(customerdialog)

        QMetaObject.connectSlotsByName(customerdialog)
    # setupUi

    def retranslateUi(self, customerdialog):
        customerdialog.setWindowTitle("")
        self.phone_label.setText(QCoreApplication.translate("customerdialog", u"Phone:", None))
        self.name_label.setText(QCoreApplication.translate("customerdialog", u"Name:", None))
        self.email_label.setText(QCoreApplication.translate("customerdialog", u"Email:", None))
        self.address_label.setText(QCoreApplication.translate("customerdialog", u"Address:   ", None))
        self.keeppen_checkbox.setText(QCoreApplication.translate("customerdialog", u"Keep window open", None))
        self.toast_success_label.setText("")
        self.toast_error_label.setText("")
        self.accept_button.setText(QCoreApplication.translate("customerdialog", u"Accept", None))
        self.cancel_button.setText(QCoreApplication.translate("customerdialog", u"Cancel", None))
    # retranslateUi

