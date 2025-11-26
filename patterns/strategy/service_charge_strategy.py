__author__ = "Nathan Natoza"
__version__ = "1.1.0"
__credits__ = ""

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    A service charge strategy class.
    This class will deal with the different
    types of strategies a service charge will have.
    """
    # Public attribute
    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract method that will call the different
        service charge strategies that will be accessed in the subclasses.
        
        Args:
            account (BankAccount): The bank accounts that will receives 
            the service charge based on the type of bank account and 
            its criteria that the service charge is applied too.

        Return:
            float: The calculated service charge amount.
        """
        pass
