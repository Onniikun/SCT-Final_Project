__author__ = "Nathan Natoza"
__version__ = "1.1.0"
__credits__ = ""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A management fee strategy class.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        A initiatizing method that will apply a management fee
        to the banking accounts.

        Args:
            date_created(date): Creation date of the bank account.
            management_fee(float): A management fee that depending 
            on age of the investment account.

        """
        self.__date_created = date_created

        self.__management_fee = management_fee

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
        if self.__date_created >= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        else:
            return self.BASE_SERVICE_CHARGE

