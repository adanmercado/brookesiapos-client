# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saleswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

class SalesWidget_UI(object):
    def setupUi(self, saleswidget):
        if not saleswidget.objectName():
            saleswidget.setObjectName(u"saleswidget")
        saleswidget.resize(1000, 741)
        saleswidget.setMinimumSize(QSize(1000, 741))
        self.horizontalLayout_5 = QHBoxLayout(saleswidget)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 8)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.barcode_lineedit = QLineEdit(saleswidget)
        self.barcode_lineedit.setObjectName(u"barcode_lineedit")
        self.barcode_lineedit.setMinimumSize(QSize(0, 45))
        self.barcode_lineedit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.barcode_lineedit)

        self.add_button = QPushButton(saleswidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(0, 45))
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"qrc/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.add_button)

        self.search_button = QPushButton(saleswidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(0, 45))
        self.search_button.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"qrc/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.search_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ticket_tableview = QTableView(saleswidget)
        self.ticket_tableview.setObjectName(u"ticket_tableview")

        self.verticalLayout_2.addWidget(self.ticket_tableview)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.remove_button = QPushButton(saleswidget)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setMinimumSize(QSize(0, 45))
        self.remove_button.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"qrc/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_button.setIcon(icon2)
        self.remove_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.remove_button)

        self.decrease_button = QPushButton(saleswidget)
        self.decrease_button.setObjectName(u"decrease_button")
        self.decrease_button.setMinimumSize(QSize(0, 45))
        self.decrease_button.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"qrc/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decrease_button.setIcon(icon3)
        self.decrease_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.decrease_button)

        self.increase_button = QPushButton(saleswidget)
        self.increase_button.setObjectName(u"increase_button")
        self.increase_button.setMinimumSize(QSize(0, 45))
        self.increase_button.setMaximumSize(QSize(16777215, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"qrc/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.increase_button.setIcon(icon4)
        self.increase_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.increase_button)

        self.customers_combobox = QComboBox(saleswidget)
        self.customers_combobox.addItem("")
        self.customers_combobox.addItem("")
        self.customers_combobox.setObjectName(u"customers_combobox")
        self.customers_combobox.setMinimumSize(QSize(200, 45))
        self.customers_combobox.setIconSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.customers_combobox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo_label = QLabel(saleswidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(0, 150))
        self.logo_label.setMaximumSize(QSize(16777215, 150))
        self.logo_label.setStyleSheet(u"")
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logo_label)

        self.saleinfo_frame = QFrame(saleswidget)
        self.saleinfo_frame.setObjectName(u"saleinfo_frame")
        self.saleinfo_frame.setMinimumSize(QSize(320, 0))
        self.saleinfo_frame.setMaximumSize(QSize(320, 16777215))
        self.saleinfo_frame.setFrameShape(QFrame.StyledPanel)
        self.saleinfo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.saleinfo_frame)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 8, 0, 8)
        self.labelSaleInfo = QLabel(self.saleinfo_frame)
        self.labelSaleInfo.setObjectName(u"labelSaleInfo")
        self.labelSaleInfo.setMinimumSize(QSize(0, 32))
        self.labelSaleInfo.setMaximumSize(QSize(16777215, 16777215))
        self.labelSaleInfo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelSaleInfo)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(12, -1, 12, -1)
        self.qty_label = QLabel(self.saleinfo_frame)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMinimumSize(QSize(0, 32))
        self.qty_label.setMaximumSize(QSize(120, 16777215))
        self.qty_label.setLayoutDirection(Qt.LeftToRight)
        self.qty_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.qty_label, 0, 0, 1, 1)

        self.qtyamount_label = QLabel(self.saleinfo_frame)
        self.qtyamount_label.setObjectName(u"qtyamount_label")
        self.qtyamount_label.setMinimumSize(QSize(120, 32))
        self.qtyamount_label.setMaximumSize(QSize(16777215, 16777215))
        self.qtyamount_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.qtyamount_label, 0, 1, 1, 1)

        self.subtotal_label = QLabel(self.saleinfo_frame)
        self.subtotal_label.setObjectName(u"subtotal_label")
        self.subtotal_label.setMinimumSize(QSize(0, 32))
        self.subtotal_label.setMaximumSize(QSize(120, 16777215))
        self.subtotal_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.subtotal_label, 1, 0, 1, 1)

        self.subtotalamount_label = QLabel(self.saleinfo_frame)
        self.subtotalamount_label.setObjectName(u"subtotalamount_label")
        self.subtotalamount_label.setMinimumSize(QSize(120, 32))
        self.subtotalamount_label.setMaximumSize(QSize(16777215, 16777215))
        self.subtotalamount_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.subtotalamount_label, 1, 1, 1, 1)

        self.taxes_label = QLabel(self.saleinfo_frame)
        self.taxes_label.setObjectName(u"taxes_label")
        self.taxes_label.setMinimumSize(QSize(0, 32))
        self.taxes_label.setMaximumSize(QSize(120, 16777215))
        self.taxes_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.taxes_label, 2, 0, 1, 1)

        self.taxesamount_label = QLabel(self.saleinfo_frame)
        self.taxesamount_label.setObjectName(u"taxesamount_label")
        self.taxesamount_label.setMinimumSize(QSize(120, 32))
        self.taxesamount_label.setMaximumSize(QSize(16777215, 16777215))
        self.taxesamount_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.taxesamount_label, 2, 1, 1, 1)

        self.total_label = QLabel(self.saleinfo_frame)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setMinimumSize(QSize(0, 32))
        self.total_label.setMaximumSize(QSize(120, 16777215))
        self.total_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.total_label, 3, 0, 1, 1)

        self.totalamount_label = QLabel(self.saleinfo_frame)
        self.totalamount_label.setObjectName(u"totalamount_label")
        self.totalamount_label.setMinimumSize(QSize(120, 32))
        self.totalamount_label.setMaximumSize(QSize(16777215, 16777215))
        self.totalamount_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.totalamount_label, 3, 1, 1, 1)

        self.change_label = QLabel(self.saleinfo_frame)
        self.change_label.setObjectName(u"change_label")
        self.change_label.setMinimumSize(QSize(0, 32))
        self.change_label.setMaximumSize(QSize(120, 16777215))
        self.change_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.change_label, 4, 0, 1, 1)

        self.changeamount_label = QLabel(self.saleinfo_frame)
        self.changeamount_label.setObjectName(u"changeamount_label")
        self.changeamount_label.setMinimumSize(QSize(120, 32))
        self.changeamount_label.setMaximumSize(QSize(16777215, 16777215))
        self.changeamount_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.changeamount_label, 4, 1, 1, 1)

        self.customer_label = QLabel(self.saleinfo_frame)
        self.customer_label.setObjectName(u"customer_label")
        self.customer_label.setMinimumSize(QSize(0, 32))
        self.customer_label.setMaximumSize(QSize(120, 16777215))
        self.customer_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.customer_label, 5, 0, 1, 1)

        self.selectedcustomer_label = QLabel(self.saleinfo_frame)
        self.selectedcustomer_label.setObjectName(u"selectedcustomer_label")
        self.selectedcustomer_label.setMinimumSize(QSize(120, 32))
        self.selectedcustomer_label.setMaximumSize(QSize(16777215, 16777215))
        self.selectedcustomer_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.selectedcustomer_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.selectedcustomer_label, 5, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.labelPayment = QLabel(self.saleinfo_frame)
        self.labelPayment.setObjectName(u"labelPayment")
        self.labelPayment.setMinimumSize(QSize(0, 32))
        self.labelPayment.setMaximumSize(QSize(16777215, 16777215))
        self.labelPayment.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelPayment)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.cashview_button = QRadioButton(self.saleinfo_frame)
        self.cashview_button.setObjectName(u"cashview_button")
        self.cashview_button.setMinimumSize(QSize(0, 36))
        self.cashview_button.setMaximumSize(QSize(16777215, 16777215))
        self.cashview_button.setLayoutDirection(Qt.LeftToRight)
        self.cashview_button.setChecked(True)

        self.horizontalLayout_3.addWidget(self.cashview_button)

        self.cardview_button = QRadioButton(self.saleinfo_frame)
        self.cardview_button.setObjectName(u"cardview_button")
        self.cardview_button.setMinimumSize(QSize(0, 36))
        self.cardview_button.setMaximumSize(QSize(16777215, 16777215))
        self.cardview_button.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.cardview_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.payment_stackwidget = QStackedWidget(self.saleinfo_frame)
        self.payment_stackwidget.setObjectName(u"payment_stackwidget")
        self.payment_stackwidget.setMinimumSize(QSize(0, 0))
        self.payment_stackwidget.setMaximumSize(QSize(16777215, 16777215))
        self.cashview = QWidget()
        self.cashview.setObjectName(u"cashview")
        self.cashview.setMaximumSize(QSize(320, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.cashview)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_4.setContentsMargins(12, 0, 12, 0)
        self.cashamount_spinbox = QDoubleSpinBox(self.cashview)
        self.cashamount_spinbox.setObjectName(u"cashamount_spinbox")
        self.cashamount_spinbox.setMinimumSize(QSize(0, 36))
        self.cashamount_spinbox.setMaximumSize(QSize(16777215, 16777215))
        self.cashamount_spinbox.setMaximum(1000000.000000000000000)

        self.verticalLayout_4.addWidget(self.cashamount_spinbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.payment_stackwidget.addWidget(self.cashview)
        self.cardview = QWidget()
        self.cardview.setObjectName(u"cardview")
        self.cardview.setMaximumSize(QSize(320, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.cardview)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, -1, 12, -1)
        self.card_label = QLabel(self.cardview)
        self.card_label.setObjectName(u"card_label")
        self.card_label.setMinimumSize(QSize(0, 45))
        self.card_label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.card_label, 0, 0, 1, 1)

        self.card_lineedit = QLineEdit(self.cardview)
        self.card_lineedit.setObjectName(u"card_lineedit")
        self.card_lineedit.setMinimumSize(QSize(0, 45))
        self.card_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.card_lineedit.setMaxLength(4)

        self.gridLayout.addWidget(self.card_lineedit, 0, 1, 1, 1)

        self.auth_lineedit = QLineEdit(self.cardview)
        self.auth_lineedit.setObjectName(u"auth_lineedit")
        self.auth_lineedit.setMinimumSize(QSize(0, 45))
        self.auth_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.auth_lineedit.setMaxLength(12)

        self.gridLayout.addWidget(self.auth_lineedit, 1, 1, 1, 1)

        self.auth_label = QLabel(self.cardview)
        self.auth_label.setObjectName(u"auth_label")
        self.auth_label.setMinimumSize(QSize(0, 45))
        self.auth_label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.auth_label, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.payment_stackwidget.addWidget(self.cardview)

        self.verticalLayout_5.addWidget(self.payment_stackwidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.finishsale_button = QPushButton(self.saleinfo_frame)
        self.finishsale_button.setObjectName(u"finishsale_button")
        self.finishsale_button.setMinimumSize(QSize(0, 45))
        self.finishsale_button.setMaximumSize(QSize(16777215, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"qrc/icons/cashregister.png", QSize(), QIcon.Normal, QIcon.Off)
        self.finishsale_button.setIcon(icon5)
        self.finishsale_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.finishsale_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.saleinfo_frame)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(saleswidget)

        self.payment_stackwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(saleswidget)
    # setupUi

    def retranslateUi(self, saleswidget):
        saleswidget.setWindowTitle("")
        self.barcode_lineedit.setPlaceholderText(QCoreApplication.translate("saleswidget", u"Scan or enter product barcode or enter a keyword to search.", None))
        self.add_button.setText(QCoreApplication.translate("saleswidget", u"Add product. Return", None))
#if QT_CONFIG(shortcut)
        self.add_button.setShortcut(QCoreApplication.translate("saleswidget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.search_button.setText(QCoreApplication.translate("saleswidget", u"Search product. F10", None))
#if QT_CONFIG(shortcut)
        self.search_button.setShortcut(QCoreApplication.translate("saleswidget", u"F10", None))
#endif // QT_CONFIG(shortcut)
        self.remove_button.setText(QCoreApplication.translate("saleswidget", u"Remove product", None))
        self.decrease_button.setText(QCoreApplication.translate("saleswidget", u"Decrease product. F6", None))
#if QT_CONFIG(shortcut)
        self.decrease_button.setShortcut(QCoreApplication.translate("saleswidget", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.increase_button.setText(QCoreApplication.translate("saleswidget", u"Increase product. F7", None))
#if QT_CONFIG(shortcut)
        self.increase_button.setShortcut(QCoreApplication.translate("saleswidget", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.customers_combobox.setItemText(0, QCoreApplication.translate("saleswidget", u"General", None))
        self.customers_combobox.setItemText(1, QCoreApplication.translate("saleswidget", u"Test", None))

        self.logo_label.setText(QCoreApplication.translate("saleswidget", u"LOGO", None))
        self.labelSaleInfo.setText(QCoreApplication.translate("saleswidget", u"SALE INFORMATION", None))
        self.qty_label.setText(QCoreApplication.translate("saleswidget", u"Qty products:", None))
        self.qtyamount_label.setText(QCoreApplication.translate("saleswidget", u"0.00", None))
        self.subtotal_label.setText(QCoreApplication.translate("saleswidget", u"Subtotal:", None))
        self.subtotalamount_label.setText(QCoreApplication.translate("saleswidget", u"$0.00", None))
        self.taxes_label.setText(QCoreApplication.translate("saleswidget", u"Taxes:", None))
        self.taxesamount_label.setText(QCoreApplication.translate("saleswidget", u"$0.00", None))
        self.total_label.setText(QCoreApplication.translate("saleswidget", u"Total:", None))
        self.totalamount_label.setText(QCoreApplication.translate("saleswidget", u"$0.00", None))
        self.change_label.setText(QCoreApplication.translate("saleswidget", u"Change:", None))
        self.changeamount_label.setText(QCoreApplication.translate("saleswidget", u"$0.00", None))
        self.customer_label.setText(QCoreApplication.translate("saleswidget", u"Client:", None))
        self.selectedcustomer_label.setText(QCoreApplication.translate("saleswidget", u"General", None))
        self.labelPayment.setText(QCoreApplication.translate("saleswidget", u"Payment", None))
        self.cashview_button.setText(QCoreApplication.translate("saleswidget", u"Cash", None))
        self.cardview_button.setText(QCoreApplication.translate("saleswidget", u"Card", None))
        self.cashamount_spinbox.setPrefix(QCoreApplication.translate("saleswidget", u"$", None))
        self.card_label.setText(QCoreApplication.translate("saleswidget", u"Card number:", None))
        self.card_lineedit.setPlaceholderText(QCoreApplication.translate("saleswidget", u"1234", None))
        self.auth_lineedit.setText("")
        self.auth_lineedit.setPlaceholderText(QCoreApplication.translate("saleswidget", u"012345678909", None))
        self.auth_label.setText(QCoreApplication.translate("saleswidget", u"Authorization number:", None))
        self.finishsale_button.setText(QCoreApplication.translate("saleswidget", u"Finish sale - F12", None))
#if QT_CONFIG(shortcut)
        self.finishsale_button.setShortcut(QCoreApplication.translate("saleswidget", u"F12", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

