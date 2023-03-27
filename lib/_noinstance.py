from abc import ABCMeta, abstractmethod

class NoInstance(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        raise TypeError("No instances of this class can be created")
