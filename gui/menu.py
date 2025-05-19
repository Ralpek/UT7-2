from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def _tratar_opcion_menu(self, opcion:int) -> bool:
        pass

    @abstractmethod
    def _visualizar_menu(self):
        pass

    @abstractmethod
    def _recoger_opcion_menu(self) -> int:
        pass