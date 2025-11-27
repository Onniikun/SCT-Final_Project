__author__ = "Nathan Natoza"
__version__ = "3.4.1"
__credits__ = ""

from datetime import date
from abc import abstractmethod, ABC
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    """
    A class for bank account infomation
    """
    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0
    
    def __init__(self,
                account_number: int, 
                client_number: int, 
                balance: float,
                date_created: date):
        """
        Initializes bank account information based on valid 
        input information such as account and client number 
        and their balance amount.

        Args:
            account_number (int): The bank account number
            client_number (int): The client's identification number
            balance (float): The amount of money the client has.
            date_created (date): Creation date of the any type of
            bank account.
        
        Raises:
            ValueError: If any parameters are blank or of
            the incorrect format.

        """
        # Inherites init method from Subject class.
        super().__init__()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number is invalid.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number is invalid.")
        
        try:
            self.__balance = float(balance) 
        except:
            self.__balance = 0

        
        if isinstance(date_created, date):
                self._date_created = date_created
        else:
            self._date_created = date.today()
#--PEP8-Standards-Line--------------------------------------------------------

    @property
    def account_number(self) -> int:
        """
        Accessor for the account_number attribute.
        
        Returns:
            int: The account number.

        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.

        Returns:
            int: The client number.

        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute.

        Returns:
            float: The client's balance amount.
        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """
        Updates the balance when the user adds an amount 
        into their account.

        Args:
            float: The updated balance.

        Returns:
            float: An updated balance.
        """
        try:
            amount = float(amount)
        except(ValueError, TypeError):
            return self.__balance
        self.__balance += float(amount)

        low_balance_message = f"Low balance warning ${self.balance:,.2f}" \
        f": on account {self.account_number}."
        large_balance_message = f"Large transaction ${amount:,.2f}" \
        f": on account {self.account_number}."

        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(low_balance_message)
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(large_balance_message)

        return self.__balance
    
    def deposit(self, amount: float) -> None:
        """
        Checks if the deposited amount is a valid datatype.

        Args:
            float: The amount being deposited.

        Raises: 
            ValueError: Raises a valueerror if the amount is not numeric 
            or not a positive number.

        """
        if not isinstance(amount, (int, float)):
            raise ValueError(
                f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(
                f"Deposit amount: ${amount:,.2f} must be positive")
        
        return self.update_balance(amount)
    
    def withdraw(self, amount: float) -> None:
        """
        Checks if the withdraw amount is valid datatype.

        Args:
            float: The amount being withdrawn.

        Raises: 
            ValueError: Raises a valueerror if the amount is not 
            numeric, negative, or exceed the account balance.

        """
        if not isinstance(amount, (int, float)):
            raise ValueError(
                f"Withdrawal amount: {amount} must be numeric.")
        if amount <=0:
            raise ValueError(
                f"Withdrawal amount: ${amount:.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(
                f"Withdrawal amount: ${amount:,.2f} "\
                f"must not exceed the account balance: "\
                f"${self.__balance:,.2f}")
        
        return self.update_balance(- amount)
    
    def __str__(self) -> str:
        """
        Returns a string of the bank account infomation
        into a formatted message.

        Returns:
            str: The Bank account instance in formatted string.
            
        """
        return(f"Account Number: {self.__account_number} " 
               f"Balance: ${self.__balance:,.2f}")

    @abstractmethod
    def get_service_charges(self) -> float:
        """
        An abstract method; Determines a
        service charge to different types of bank
        accounts based on their type.

        Returns:
            float: The service charge amount.
        """
        pass

    def attach(self, observer: Observer) -> None:
        """
        Attaches the observer to the subject list of observers.

        Args:
            observer (Observer): The observer to attach to.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detaches the observer to the subject list of observers.

        Args:
            observer (Observer): The observer to detach from.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notify the observers list of any state changes.

        Args:
            message (str): The message stating the observer
            list has changed.
        """
        for observer in self._observers:
            observer.update(message)