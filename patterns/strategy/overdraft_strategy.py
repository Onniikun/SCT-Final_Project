__author__ = "Nathan Natoza"
__version__ = "1.1.0"
__credits__ = ""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    A Overdraft strategy class.
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        A initiatizing method that will apply an overdraft_limit and
        overdraft rate to the banking accounts.

        Args:
            overdraft_limit (float): The max amount a balance 
            can be overdrawn.
            overdraft_rate (float): The rate of overdraft 
            fees being applied.

        """
        self.__overdraft_limit = overdraft_limit

        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
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
        if account.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - account.balance ) * \
            self.__overdraft_rate
            return self.BASE_SERVICE_CHARGE + service_charge