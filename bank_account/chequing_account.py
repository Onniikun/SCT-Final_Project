__author__ = "Nathan Natoza"
__version__ = "1.3.5"
__credits__ = ""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    A subclass to the bank account class;
    Chequing account infomation class.
    """
    def __init__(self,
                account_number: int, 
                client_number: int, 
                balance: float,
                date_created: date,
                overdraft_limit: float,
                overdraft_rate: float):
        """
        Initializes chequing account information based on 
        valid input information such as account and client 
        number and their balance amount.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client's identification number.
            balance (float): The amount of money the client has.
            date_created (date): Creation date of the chequing account.
            overdraft_limit (float): The max amount a balance 
            can be overdrawn.
            overdraft_rate (float): The rate of overdraft 
            fees being applied.
        
        Raises:
            ValueError: If any parameters are blank or of
            the incorrect format.

        """
        super().__init__(account_number, 
                         client_number, 
                         balance, 
                         date_created)
        
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.00

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

    def __str__(self) -> str:
        """
        Returns a string of the chequing account infomation
        into a formatted message.

        Returns:
            str: The chequing account instance in formatted string.
        """
        percent_formatting = f"{(self.__overdraft_rate * 100):.2f}"
        message = super().__str__()
        message += (f"\nOverdraft limit: ${self.__overdraft_limit:.2f}" \
                    f" Overdraft rate: {percent_formatting}%" \
                    f" Account Type: Chequing.")
        return message

    def get_service_charges(self) -> float:
        """
        Checks if the chequing account balance is greater or
        less than the overdraft limit. If the balance is less 
        than the overdraft limit a serivce charge is applied.

        Returns:
            float: The calculated service based on overdraft 
            limit, rate and chequing account balance.
        """
        return self.__strategy.calculate_service_charges(self)