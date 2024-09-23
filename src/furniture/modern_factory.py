from src.furniture.base import FurnitureFactory, Chair, Table


class ModernChair(Chair):
    def sit_on(self) -> None:
        print("Sitting on a modern chair.")


class ModernTable(Table):
    def place_items(self) -> None:
        print("Placing items on a modern table.")


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()
