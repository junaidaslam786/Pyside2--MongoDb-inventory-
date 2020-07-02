from main import *

from PySide2 import QtWidgets, QtCore, QtGui

# from models.models import *
import databaseOperations


class Customer:

    # def __init__(self):
    #     self.customer = CustomerModel()

    def show_customer(self):
        self.ui.Pages_Widget.setCurrentWidget(self.ui.customer_page)

    def add_customer(self):
        # self.customer = CustomerModel(
        #     first_name=self.ui.customer_fname_le.text(),
        #     last_name=self.ui.customer_lname_le.text(),
        #     phone_no=self.ui.customer_phone_le.text(),
        #     office_no=self.ui.customer_office_le.text(),
        #     email=self.ui.customer_email_le.text(),
        #     address=self.ui.customer_address_le.text()
        # )
        # self.customer.save()
        self.customer = {
            'first_name': self.ui.customer_fname_le.text(),
            'last_name': self.ui.customer_lname_le.text(),
            'phone_no': self.ui.customer_phone_le.text(),
            'office_no': self.ui.customer_office_le.text(),
            'email': self.ui.customer_email_le.text(),
            'address': self.ui.customer_address_le.text()
        }
        databaseOperations.collection.insert_one(self.customer)

        self.ui.customer_fname_le.setText('')
        self.ui.customer_lname_le.setText('')
        self.ui.customer_phone_le.setText('')
        self.ui.customer_office_le.setText('')
        self.ui.customer_email_le.setText('')
        self.ui.customer_address_le.setText('')


class CustomerTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self.customer_data = data
        self.columns = list(self.customer_data[0].keys())

    def flags(self, index):

        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        elif index.column() == 1:
            return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):

        return len(self.customer_data)

    def columnCount(self, *args, **kwargs):

        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[section].title()

    def data(self, index, role):

        row = self.customer_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.DisplayRole:
            return str(row[column])

    def setData(self, index, value, role=QtCore.Qt.EditRole):

        if index.isValid():
            selected_row = self.customer_data[index.row()]
            selected_column = self.columns[index.column()]
            selected_row[selected_column] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole,))
            ok = databaseOperations.update_existing(selected_row['_id'], selected_row)
            if ok:
                return True
        return False

    def insertRows(self):
        row_count = len(self.customer_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = {key: None for key in self.columns if not key == '_id'}
        document_id = databaseOperations.insert_data(empty_data)
        new_data = databaseOperations.get_single_data(document_id)
        self.customer_data.append(new_data)
        row_count += 1
        self.endInsertRows()
        return True

    def removeRows(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.customer_data[row_id]['_id']
        databaseOperations.remove_data(document_id)
        self.customer_data.pop(row_id)
        self.endRemoveRows()
        return True


class InLineEditDelegate(QtWidgets.QItemDelegate):
    """
    Delegate is important for inline editing of cells
    """

    def createEditor(self, parent, option, index):
        return super(InLineEditDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        text = index.data(QtCore.Qt.EditRole) or index.data(QtCore.Qt.DisplayRole)
        editor.setText(str(text))
