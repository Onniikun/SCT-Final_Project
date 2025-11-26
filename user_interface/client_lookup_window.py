__author__ = "ACE Faculty"
__version__ = "2.0.0"
__credits__ = "Nathan Natoza"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A client look up window class to find
    client banking infomation and account
    """
    __client_listing = {}
    __accounts = {}

    def __init__(self):
        """
        """
        super().__init__()
        self.__client_listing, self.__accounts = load_data()
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)
        
    @Slot()   
    def __on_lookup_client(self) -> None:
        """
        Searches for client bank account and displays bank account 
        information like client number, balance, etc.
        Raises:
            ValueError: If the amount not numeric, doesnt exist,
            or if the program doesnt run properly.
        """
        try:
            client_number_text = self.client_number_edit.text().strip()

            try:
                client_number = int(client_number_text)
            except ValueError: 
                QMessageBox.information(self, "Input Error",
                            "Client number must be a numeric value.")
                self.reset_display()
                return

            if client_number not in self.__client_listing:
                QMessageBox.information(self, "Not Found", 
                                    f"Client number: {client_number} not found.")
                self.reset_display()
                return
            
            if client_number in self.__client_listing:
                client = self.__client_listing[client_number]
                full_name = f"Client Name: {client.first_name} {client.last_name}"
                self.client_info_label.setText(full_name)
    
            self.account_table.setRowCount(0)
            
            row_position = 0
            for account in self.__accounts.values():
                if account.client_number == client_number:
                    self.account_table.insertRow(row_position)

                    account_number_item = QTableWidgetItem(
                        str(account.account_number))
                    account_number_item.setTextAlignment(
                        Qt.AlignCenter | Qt.AlignVCenter)

                    balance_item = QTableWidgetItem(
                        f"${account.balance:,.2f}")
                    balance_item.setTextAlignment(
                        Qt.AlignRight | Qt.AlignVCenter)

                    date_created_item = QTableWidgetItem(
                        str(account._date_created)) 
                    date_created_item.setTextAlignment(
                        Qt.AlignCenter | Qt.AlignVCenter)

                    account_type_item = QTableWidgetItem(
                        account.__class__.__name__)
                    account_type_item.setTextAlignment(
                        Qt.AlignCenter | Qt.AlignVCenter)

                    self.account_table.setItem(row_position, 0, 
                                               account_number_item)
                    self.account_table.setItem(row_position, 1, 
                                               balance_item)
                    self.account_table.setItem(row_position, 2, 
                                               date_created_item)
                    self.account_table.setItem(row_position, 3, 
                                               account_type_item)

                    row_position += 1

            self.account_table.resizeColumnsToContents()
            self.__toggle_filter_clicked(False)


        except Exception as e:
            QMessageBox.information(self, "Error",
                    f"An unexpected error occurred: {str(e)}")
        
    @Slot()        
    def __on_text_changed(self):
        """
        Clears the account table upon making changes.
        """
        self.account_table.setRowCount(0)
        self.client_info_label.clear()

    @Slot()
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Displays account information for each bank account.

        Args:
            row(int): The account number.
            column(int): The account number.
        """
        try:
            selected_account = self.account_table.item(row, 0)
            if selected_account is None: 
                QMessageBox.information(self, "Invalid Selection",
                                    "Please select a valid record.")
                return
            
            try:
                account_number = int(selected_account.text().strip())

            except ValueError:
                QMessageBox.information(self, "Invalid Account Number",
                              "Account number must be a valid integer.")
                
            if account_number not in self.__accounts:
                QMessageBox.information(self, "No Bank Account",
                                    "Bank Account selected does not exist.")
                return
            
            account_details = AccountDetailsWindow(
                self.__accounts[account_number])
            account_details.balance_updated.connect(self.__update_data)
            account_details.exec()
            
        except Exception as e:
            QMessageBox.information(self, "Error",
                    f"An unexpected error occurred: {str(e)}")
            

    @Slot()
    def __update_data(self, account: BankAccount) -> None:
        """
        Updates bank account data after making deposits
        and or withdrawals

        Args:
            account(BankAccount): The account thats getting changed.
        """
        for row in range(self.account_table.rowCount()):
            if int(self.account_table.item(row, 0).text()) == \
            account.account_number:
                self.__accounts[account.account_number] = account
                update_data(account)
                self.account_table.item(row, 1).setText(
                    f"${account.balance:,.2f}")
                
    @Slot()           
    def __on_filter_clicked(self):
        """
        Filter button that displays the filtered data 
        depeneding on the filtering criteria.
        """
        filter_value = self.filter_combo_box.currentIndex()
        filter_value_text = self.filter_edit.text().strip().lower()

        row_count = self.account_table.rowCount()

        for row in range(row_count):
            item = self.account_table.item(row, filter_value)

            if item is not None and filter_value_text in item.text().lower():
                self.account_table.setRowHidden(row, False)
            else:
                self.account_table.setRowHidden(row, True)


    def __toggle_filter_clicked(self, filter_on: bool):
        """
        A toggle filter if the user want the data to be filtered.

        Args: 
            filter_on (bool): button is enabled to true or false
            if the data is currently being filtered.
        """
        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is currently filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_label.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
