from dataclasses import dataclass
from fruitvegetable import FruitVegetable


@dataclass
class Shop:
    product_list: list[FruitVegetable]

    def __init__(self, product_list=None):
        if product_list is None:
            product_list = [
                FruitVegetable("Clémentine", 6_000, 2.9, False),
                FruitVegetable("Datte", 4_000, 7, False),
                FruitVegetable("Grenade", 3_000, 3.5, False),
                FruitVegetable("Kaki", 3_000, 4.5, False),
                FruitVegetable("Kiwi", 5_000, 3.5, False),
                FruitVegetable("Mandarine", 6_000, 2.8, False),
                FruitVegetable("Orange", 8_000, 1.5, False),
                FruitVegetable("Pamplemousse", 8, 2, True),
                FruitVegetable("Poire", 5_000, 2.5, False),
                FruitVegetable("Pomme", 8_000, 1.5, False),
                FruitVegetable("Carotte", 7_000, 1.3, False),
                FruitVegetable("Choux de Bruxelles", 4_000, 4, False),
                FruitVegetable("Chou vert", 12, 2.5, True),
                FruitVegetable("Courge butternut", 6, 2.5, True),
                FruitVegetable("Endive", 5_000, 2.5, False),
                FruitVegetable("Épinard", 4_000, 2.6, False),
                FruitVegetable("Poireau", 5_000, 1.2, False),
                FruitVegetable("Potiron", 6, 2.5, True),
                FruitVegetable("Radis noir", 10, 5, True),
                FruitVegetable("Salsifis", 3_000, 2.5, False)
            ]
        self.product_list: list[FruitVegetable] = product_list

    def __str__(self) -> str:
        display_balance_sheet: str = "Voici le stock disponible:\n"

        for product in self.product_list:
            display_balance_sheet += f"{product.name}: {product.quantity}"
            if product.is_unit:
                display_balance_sheet += " pièces"
            else:
                display_balance_sheet += "g"

        return display_balance_sheet

    def nb_fruit_vegetable(self):
        return len(self.product_list)
