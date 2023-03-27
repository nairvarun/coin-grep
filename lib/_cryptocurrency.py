from abc import ABCMeta, abstractclassmethod
from _noinstance import NoInstance

class Cryptocurrency(NoInstance, metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def derive():
        pass

    @abstractclassmethod
    def validate():
        pass

    @abstractclassmethod
    def get_info():
        pass
