from src.furniture.base import FurnitureFactory
from src.furniture.classic_factory import ClassicFurnitureFactory
from src.furniture.modern_factory import ModernFurnitureFactory


def furnish_room(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()

    chair.sit_on()
    table.place_items()


if __name__ == "__main__":
    if __name__ == "__main__":
        modern_factory = ModernFurnitureFactory()
        classic_factory = ClassicFurnitureFactory()

        print("Furnishing modern room:")
        furnish_room(modern_factory)

        print("Furnishing classic room:")
        furnish_room(classic_factory)
