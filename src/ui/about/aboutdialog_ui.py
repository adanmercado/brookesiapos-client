# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class AboutDialog_UI(object):
    def setupUi(self, aboutdialog):
        if not aboutdialog.objectName():
            aboutdialog.setObjectName(u"aboutdialog")
        aboutdialog.resize(500, 500)
        aboutdialog.setMinimumSize(QSize(500, 500))
        self.verticalLayout = QVBoxLayout(aboutdialog)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.info_label = QLabel(aboutdialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMinimumSize(QSize(0, 32))
        self.info_label.setTextFormat(Qt.MarkdownText)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.info_label)

        self.license_textedit = QPlainTextEdit(aboutdialog)
        self.license_textedit.setObjectName(u"license_textedit")
        self.license_textedit.setMinimumSize(QSize(0, 180))
        self.license_textedit.setTabChangesFocus(True)
        self.license_textedit.setUndoRedoEnabled(False)
        self.license_textedit.setReadOnly(True)

        self.verticalLayout.addWidget(self.license_textedit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.accept_button = QPushButton(aboutdialog)
        self.accept_button.setObjectName(u"accept_button")
        self.accept_button.setMinimumSize(QSize(0, 45))
        icon = QIcon()
        icon.addFile(u"qrc/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accept_button.setIcon(icon)
        self.accept_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.accept_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(aboutdialog)

        QMetaObject.connectSlotsByName(aboutdialog)
    # setupUi

    def retranslateUi(self, aboutdialog):
        aboutdialog.setWindowTitle("")
        self.info_label.setText("")
        self.accept_button.setText(QCoreApplication.translate("aboutdialog", u"Accept", None))
    # retranslateUi

