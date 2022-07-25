# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customerswidget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class CustomersWidget_UI(object):
    def setupUi(self, customerswidget):
        if not customerswidget.objectName():
            customerswidget.setObjectName(u"customerswidget")
        customerswidget.resize(1000, 600)
        customerswidget.setMinimumSize(QSize(1000, 600))
        self.verticalLayout = QVBoxLayout(customerswidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.customers_tableview = QTableView(customerswidget)
        self.customers_tableview.setObjectName(u"customers_tableview")
        self.customers_tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customers_tableview.setAlternatingRowColors(True)
        self.customers_tableview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.customers_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.customers_tableview.setShowGrid(False)
        self.customers_tableview.horizontalHeader().setDefaultSectionSize(300)
        self.customers_tableview.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.customers_tableview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_button = QPushButton(customerswidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(0, 45))
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"qrc/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.add_button)

        self.edit_button = QPushButton(customerswidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(0, 45))
        self.edit_button.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"qrc/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_button.setIcon(icon1)
        self.edit_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.edit_button)

        self.delete_button = QPushButton(customerswidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(0, 45))
        self.delete_button.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"qrc/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon2)
        self.delete_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.delete_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(customerswidget)

        QMetaObject.connectSlotsByName(customerswidget)
    # setupUi

    def retranslateUi(self, customerswidget):
        customerswidget.setWindowTitle("")
        self.add_button.setText(QCoreApplication.translate("customerswidget", u"Add client", None))
        self.edit_button.setText(QCoreApplication.translate("customerswidget", u"Modify selected", None))
        self.delete_button.setText(QCoreApplication.translate("customerswidget", u"Delete selected", None))
    # retranslateUi

