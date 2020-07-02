# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 794)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgba(230, 230, 230, 230);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(80, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QToolButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(170, 85, 0);\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u":/icon/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_top)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_top)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QSize(80, 0))
        self.frame_left_menu.setMaximumSize(QSize(80, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgba(225, 225, 225, 225);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        sizePolicy.setHeightForWidth(self.frame_top_menus.sizePolicy().hasHeightForWidth())
        self.frame_top_menus.setSizePolicy(sizePolicy)
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Home = QPushButton(self.frame_top_menus)
        self.Btn_Home.setObjectName(u"Btn_Home")
        self.Btn_Home.setMinimumSize(QSize(0, 40))
        self.Btn_Home.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 127);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Home.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.Btn_Home)

        self.Btn_Customer = QPushButton(self.frame_top_menus)
        self.Btn_Customer.setObjectName(u"Btn_Customer")
        self.Btn_Customer.setMinimumSize(QSize(0, 40))
        self.Btn_Customer.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Customer)

        self.Btn_Product = QPushButton(self.frame_top_menus)
        self.Btn_Product.setObjectName(u"Btn_Product")
        self.Btn_Product.setMinimumSize(QSize(0, 40))
        self.Btn_Product.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Product)

        self.Btn_Sales = QPushButton(self.frame_top_menus)
        self.Btn_Sales.setObjectName(u"Btn_Sales")
        self.Btn_Sales.setMinimumSize(QSize(0, 40))
        self.Btn_Sales.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Sales)

        self.Btn_Order = QPushButton(self.frame_top_menus)
        self.Btn_Order.setObjectName(u"Btn_Order")
        self.Btn_Order.setMinimumSize(QSize(0, 40))
        self.Btn_Order.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Order)

        self.Btn_Supplier = QPushButton(self.frame_top_menus)
        self.Btn_Supplier.setObjectName(u"Btn_Supplier")
        self.Btn_Supplier.setMinimumSize(QSize(0, 40))
        self.Btn_Supplier.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Supplier)

        self.Btn_Transactions = QPushButton(self.frame_top_menus)
        self.Btn_Transactions.setObjectName(u"Btn_Transactions")
        self.Btn_Transactions.setMinimumSize(QSize(0, 40))
        self.Btn_Transactions.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Transactions)

        self.Btn_Billing = QPushButton(self.frame_top_menus)
        self.Btn_Billing.setObjectName(u"Btn_Billing")
        self.Btn_Billing.setMinimumSize(QSize(0, 40))
        self.Btn_Billing.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Billing)

        self.Btn_Reports = QPushButton(self.frame_top_menus)
        self.Btn_Reports.setObjectName(u"Btn_Reports")
        self.Btn_Reports.setMinimumSize(QSize(0, 40))
        self.Btn_Reports.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgba(225, 225, 225, 225);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Reports)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.Pages_Widget.addWidget(self.home_page)
        self.customer_page = QWidget()
        self.customer_page.setObjectName(u"customer_page")
        self.verticalLayout_6 = QVBoxLayout(self.customer_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.customer_frame_header = QFrame(self.customer_page)
        self.customer_frame_header.setObjectName(u"customer_frame_header")
        self.customer_frame_header.setMinimumSize(QSize(0, 0))
        self.customer_frame_header.setMaximumSize(QSize(16777215, 30))
        self.customer_frame_header.setStyleSheet(u"background-color: rgb(179, 179, 179);")
        self.customer_frame_header.setFrameShape(QFrame.NoFrame)
        self.customer_frame_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.customer_frame_header)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.customer_frame_header)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.customer_frame_header)

        self.frame_2 = QFrame(self.customer_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_customer_box = QGroupBox(self.frame)
        self.add_customer_box.setObjectName(u"add_customer_box")
        self.add_customer_box.setMaximumSize(QSize(500, 500))
        self.add_customer_box.setStyleSheet(u"* {\n"
"	color: rgb(85, 85, 127);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	border-color: rgb(0, 0, 0);\n"
"}\n"
"QpushButton:hover {\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        self.add_customer_box.setFlat(False)
        self.gridLayout = QGridLayout(self.add_customer_box)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.customer_address_le = QLineEdit(self.add_customer_box)
        self.customer_address_le.setObjectName(u"customer_address_le")
        self.customer_address_le.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.customer_address_le, 5, 1, 1, 1)

        self.Btn_add_customer = QPushButton(self.add_customer_box)
        self.Btn_add_customer.setObjectName(u"Btn_add_customer")
        self.Btn_add_customer.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Btn_add_customer, 6, 0, 1, 2)

        self.label_6 = QLabel(self.add_customer_box)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.customer_phone_le = QLineEdit(self.add_customer_box)
        self.customer_phone_le.setObjectName(u"customer_phone_le")
        self.customer_phone_le.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.customer_phone_le, 2, 1, 1, 1)

        self.customer_email_le = QLineEdit(self.add_customer_box)
        self.customer_email_le.setObjectName(u"customer_email_le")
        self.customer_email_le.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.customer_email_le, 4, 1, 1, 1)

        self.customer_fname_le = QLineEdit(self.add_customer_box)
        self.customer_fname_le.setObjectName(u"customer_fname_le")
        self.customer_fname_le.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.customer_fname_le, 0, 1, 1, 1)

        self.label_5 = QLabel(self.add_customer_box)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.customer_lname_le = QLineEdit(self.add_customer_box)
        self.customer_lname_le.setObjectName(u"customer_lname_le")
        self.customer_lname_le.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.customer_lname_le, 1, 1, 1, 1)

        self.label_4 = QLabel(self.add_customer_box)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_7 = QLabel(self.add_customer_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.customer_office_le = QLineEdit(self.add_customer_box)
        self.customer_office_le.setObjectName(u"customer_office_le")
        self.customer_office_le.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.customer_office_le, 3, 1, 1, 1)

        self.label_3 = QLabel(self.add_customer_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_8 = QLabel(self.add_customer_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.add_customer_box)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.search_customer_box = QGroupBox(self.frame_4)
        self.search_customer_box.setObjectName(u"search_customer_box")
        self.search_customer_box.setLayoutDirection(Qt.LeftToRight)
        self.search_customer_box.setStyleSheet(u"* {\n"
"	color: rgb(85, 85, 127);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	border-color: rgb(0, 0, 0);\n"
"}\n"
"QpushButton:hover {\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.search_customer_box)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.search_customer_box)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.customer_search_le = QLineEdit(self.search_customer_box)
        self.customer_search_le.setObjectName(u"customer_search_le")

        self.gridLayout_2.addWidget(self.customer_search_le, 0, 1, 1, 1)

        self.Btn_search_customer = QPushButton(self.search_customer_box)
        self.Btn_search_customer.setObjectName(u"Btn_search_customer")

        self.gridLayout_2.addWidget(self.Btn_search_customer, 1, 0, 1, 2)


        self.verticalLayout_10.addWidget(self.search_customer_box)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Btn_update_customer = QPushButton(self.frame_5)
        self.Btn_update_customer.setObjectName(u"Btn_update_customer")
        self.Btn_update_customer.setStyleSheet(u"color: rgb(85, 85, 127);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	border-color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.Btn_update_customer)

        self.Btn_delete_customer = QPushButton(self.frame_5)
        self.Btn_delete_customer.setObjectName(u"Btn_delete_customer")
        self.Btn_delete_customer.setStyleSheet(u"color: rgb(85, 85, 127);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	border-color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.Btn_delete_customer)


        self.verticalLayout_10.addWidget(self.frame_5)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_9.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_4.addWidget(self.tableView)


        self.verticalLayout_9.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.Pages_Widget.addWidget(self.customer_page)
        self.sales_page = QWidget()
        self.sales_page.setObjectName(u"sales_page")
        self.Pages_Widget.addWidget(self.sales_page)
        self.product_page = QWidget()
        self.product_page.setObjectName(u"product_page")
        self.Pages_Widget.addWidget(self.product_page)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rice Management", None))
        self.Btn_Home.setText("")
        self.Btn_Customer.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.Btn_Product.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.Btn_Sales.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.Btn_Order.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.Btn_Supplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.Btn_Transactions.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.Btn_Billing.setText(QCoreApplication.translate("MainWindow", u"Biling", None))
        self.Btn_Reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.add_customer_box.setTitle(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.Btn_add_customer.setText(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Office No: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone No: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last Name: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email ID: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"First Name: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Address: ", None))
        self.search_customer_box.setTitle(QCoreApplication.translate("MainWindow", u"Search Box", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Customer Search: ", None))
        self.Btn_search_customer.setText(QCoreApplication.translate("MainWindow", u"Search Customer", None))
        self.Btn_update_customer.setText(QCoreApplication.translate("MainWindow", u"Update Customer", None))
        self.Btn_delete_customer.setText(QCoreApplication.translate("MainWindow", u"Delete Customer", None))
    # retranslateUi

