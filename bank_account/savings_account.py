__author__ = "Nathan Natoza"
__version__ = "1.3.4"
__credits__ = ""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    A subclass to the bank account class;
    Savings account infomation class.
    """
    # Public attribute
    SERVICE_CHARGE_PREMIUM: float = 2.0  
    
    def __init__(self,
                account_number: int, 
                client_number: int, 
                balance: float,
                date_created: date,
                minimum_balance: float):
        """
        Initializes chequing account information based on 
        valid input information such as account and client 
        number and their balance amount.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client's identification number.
            balance (float): The amount of money the client has.
            date_created (date): Creation date of the savings account.
            minimum_balance (float): The minimum balance amount for
            premium service charge calculation.
        
        Raises:
            ValueError: If any parameters are blank or of
            the incorrect format.

        """
        super().__init__(account_number, 
                         client_number, 
                         balance, 
                         date_created)
        
        self.__strategy = MinimumBalanceStrategy(minimum_balance)

        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50
        
    def __str__(self) -> str:
        """
        Returns a string of the savings account infomation
        into a formatted message.

        Returns:
            str: The savings account instance in formatted string.
        """
        message = super().__str__()
        message += (f"\nMinimum Balance: ${self.__minimum_balance:,.2f}" \
                    f" Account Type: Savings.")
        return message
        
    def get_service_charges(self) -> float:
        """
        Checks if the savings account balance is greater or equal
        than the minimum balance if it is then sets base service
        charge. If not, multiply with service premium charge 
        on top of that.

        Returns:
            float: Returns the base service charge or
            a base service charge multiplied by the
            service charge premium.
        """
        return self.__strategy.calculate_service_charges(self)
