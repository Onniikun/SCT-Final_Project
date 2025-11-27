__author__ = "Nathan Natoza"
__version__ = "1.1.0"
__credits__ = ""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    A minimum balance strategy class.
    """
    # Public attribute
    SERVICE_CHARGE_PREMIUM: float = 2.0  
    
    def __init__(self, minimum_balance: float):
        """
        A initiatizing method that will apply an overdraft_limit and
        overdraft rate to the banking accounts.

        Args:
            minimum_balance (float): The minimum balance amount for
            premium service charge calculation.

        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount):
        """
        Applies the calculated service charges after a strategy is 
        applied to it.

        Args:
            account (BankAccount): The bank accounts that the 
            strategies will be applied to.
            
        Returns:
            float: Returns the calculated service charges after the
            strategy is applied.
        """
        if account.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            service_fee = self.BASE_SERVICE_CHARGE * \
            self.SERVICE_CHARGE_PREMIUM
            return service_fee