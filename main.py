import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *






# GUI FILE

from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

# Import Customer
from customer import *

import databaseOperations

from models.models import *



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        ## Current Page
        self.ui.Pages_Widget.setCurrentWidget(self.ui.home_page)

        self.ui.Btn_Customer.clicked.connect(lambda: Customer.show_customer(self))
        self.ui.Btn_add_customer.clicked.connect(lambda: Customer.add_customer(self))


        self.ui.Btn_Home.clicked.connect(self.show_home)

        # self.customer_data = CustomerModel.objects()
        # for i in self.customer_data[:]:
        #     data = [i.first_name, i.last_name, i.phone_no, i.office_no, i.email, i.address]
        # self.model = CustomerTableModel(data)
        # self.ui.tableView.setModel(self.model)
        # for i in customer:
        #     result = [i.first_name, i.last_name, i.phone_no, i.office_no, i.email, i.address]
        #     print(result)
        #     for key in customer[0]:
        #         print(key)key
        self.customer_data = databaseOperations.get_multiple_data()
        self.model = CustomerTableModel(self.customer_data)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setItemDelegate(InLineEditDelegate())
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.context_menu)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(50)
        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.hideColumn(0)



        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def context_menu(self):
        menu = QtWidgets.QMenu()
        add_data = menu.addAction("Add New Data")
        # add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: self.model.insertRows())
        if self.ui.tableView.selectedIndexes():
            remove_data = menu.addAction("Remove Data")
            # remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: self.model.removeRows(self.ui.tableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())



    def show_home(self):
        self.ui.Pages_Widget.setCurrentWidget(self.ui.home_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
