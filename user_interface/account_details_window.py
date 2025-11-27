__author__ = "ACE Faculty"
__version__ = "2.0.0"
__credits__ = "Nathan Natoza"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        if isinstance(account, BankAccount):
            self.__account = copy.deepcopy(account)
        else:
            self.reject()
            
        self.account_number_label.setText(f"{self.__account.account_number}")
        self.balance_label.setText(f"${self.__account.balance:,.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)


    @Slot()
    def __on_apply_transaction(self) -> None:
        """
        This method applies transaction functionally
        such as deposit and withdrawal. Clears any
        previous banking data.
        """
        try:
            account_amount = float(
                self.transaction_amount_edit.text().strip())
        except ValueError:
                QMessageBox.information(self, "Invalid Data",
                                    "Amount must be numeric.")
                return
        try:
            if self.sender() == self.deposit_button:
                sender = "Deposit"
                self.__account.deposit(account_amount)
            elif self.sender() == self.withdraw_button:
                sender = "Withdrawal"
                self.__account.withdraw(account_amount)
            
            self.balance_label.setText(
                f"${self.__account.balance:,.2f}")
            self.balance_updated.emit(self.__account)
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            QMessageBox.information(self, f"{sender} Failed",
                    f"{e}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    @Slot()
    def __on_exit(self) -> None:
        """
        Closes the deposit and withdraw display window.
        """
        self.close()


        
