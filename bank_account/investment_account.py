__author__ = "Nathan Natoza"
__version__ = "1.3.4"
__credits__ = ""

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    A subclass to the bank account class;
    Investment account infomation class.
    """
    # Public attribute
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self,
                account_number: int, 
                client_number: int, 
                balance: float,
                date_created: date,
                management_fee: float):
        """
        Initializes chequing account information based on 
        valid input information such as account and client 
        number and their balance amount.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client's identification number.
            balance (float): The amount of money the client has.
            date_created (date): Creation date of the 
            investment account.
            management_fee (float): A management fee that depending 
            on age of the investment account.
        
        Raises:
            ValueError: If any parameters are blank or of
            the incorrect format.

        """
        super().__init__(account_number, 
                         client_number, 
                         balance, 
                         date_created)
        

        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

    def __str__(self) -> str:
        """
        Returns a string of the investment account infomation
        into a formatted message.

        Returns:
            str: The investment account instance in formatted string.
        """            
        if self._date_created >= self.TEN_YEARS_AGO:    
            fee = f"${self.__management_fee:.2f}" 
        else:
            fee = "Waived"

        message = super().__str__()
        message += (f"\nDate Created: {self._date_created} " \
                    f"Management Fee: {fee}" \
                    f" Account Type: Investment.")
        return message
    
    def get_service_charges(self) -> float:
        """
        Checks if the investment account is more than
        10 years old and adds a base service charge.
        If not then adds on an management fee.

        Returns:
            float: The service charge with or a management fee.
        """
        return self.__strategy.calculate_service_charges(self)