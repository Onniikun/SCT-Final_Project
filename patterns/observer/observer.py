__author__ = "Nathan Natoza"
__version__ = "1.1.0"
__credits__ = ""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    An observer class for observing messages and any state
    changes that happened to subject file.
    """
    @abstractmethod
    def update(self, message: str):
        """
        Abstract method that will pass on 
        the message to the client.

        Args:
            Message (str): The message alerting the user
            to any changes.
        """
        pass