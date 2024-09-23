from abc import abstractmethod, ABC


class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> None:
        pass


class Table(ABC):
    @abstractmethod
    def place_items(self) -> None:
        pass


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass
