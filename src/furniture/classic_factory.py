from src.furniture.base import FurnitureFactory, Chair, Table


class ClassicChair(Chair):
    def sit_on(self) -> None:
        print("Sitting on a classic chair.")


class ClassicTable(Table):
    def place_items(self) -> None:
        print("Placing items on a classic table.")


class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ClassicChair()

    def create_table(self) -> Table:
        return ClassicTable()
