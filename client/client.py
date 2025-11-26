__author__ = "Nathan Natoza"
__version__ = "1.4.1"
__credits__ = ""


from email_validator import EmailNotValidError, validate_email
from abc import abstractmethod
from utility.file_utils import simulate_send_email
from datetime import date
from patterns.observer.observer import Observer

class Client(Observer):
    """
    A class on bank client's information.
    """

    def __init__(self, 
                 client_number: int, 
                 first_name: str, 
                 last_name: str, 
                 email_address: str):
        """
        Initializes client's information based on valid inputs 
        information such as client number, first and last name,
        and their email address.

        Args:
            client_number (int): The client's id number.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
            email_address (str): The email address of the client.
        
        Raises:
            ValueError: If any parameters are invalid or blank.
            EmailNotValidError: If email given isnt valid.

        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Invalid client number.")
        
        if len(first_name.strip()) != 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name input cannot be blank.")
        
        if len(last_name.strip()) != 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name input cannot be blank.")

        try:
            validated_email = validate_email(
                email_address, check_deliverability = False)  
            self.__email_address = validated_email.normalized
        except EmailNotValidError as e:
            self.__email_address = "email@pixell-river.com"
        
#--PEP8-Standards-Line--------------------------------------------------------

    @property
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.

        Returns:
            int: The client number.

        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Accessor for the first_name attribute.
        
        Returns:
            str: The first_name of the client.

        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Accessor for the first_name attribute.

        Returns:
            str: The last_name of the client.

        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for the email_address attribute.

        Returns:
            str: The email address of the client.

        """
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns a string of the client's first and last name 
        as well as their client number and email address.
        
        Returns:
            str: The Client instance in formatted string.
            
        """
        return(f"{self.__first_name}, {self.__last_name}, " \
               f"[{self.__client_number}] - {self.__email_address}")

    def update(self, message: str):
        """
        Alerts and sends a message to the user about any changes to
        any type of bank accounts.

        Args:
            str (message): The message alerting the user.
        """
        subject_message = f"ALERT: Unusual Activity: {date.today()}"
        message_2 = f"Notification for {self.__client_number}: " \
        f"{self.__first_name} {self.__last_name}: {message}"

        simulate_send_email(self.__email_address, subject_message, message_2)