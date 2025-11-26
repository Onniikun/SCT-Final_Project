__author__ = "Nathan Natoza"
__version__ = "1.2.0"
__credits__ = ""

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    A subject class for maintaining messages and notfiying 
    the user for any changes.
    """
    def __init__(self):
        """
        Initializes the observer list.
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attaches the observer to the subject list of observers.

        Args:
            observer (Observer): The observer to attach to.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detaches the observer to the subject list of observers.

        Args:
            observer (Observer): The observer to deattach from.
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Notify the observers list of any state changes.

        Args:
            message (str): The message stating the observer
            list has changed.
        """
        pass