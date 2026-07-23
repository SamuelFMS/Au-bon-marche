from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar
from fruitvegetable import FruitVegetable


@dataclass
class Product:
    product_list: ClassVar[list["FruitVegetable"]]

    def __post_init__(self):
        FruitVegetable.product_list = [
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

    def __str__(self) -> str:
        display_bilan: str = "Voici le sock disponible:\n"

        for product in self.product_list:
            display_bilan += f"{product.name}: {product.quantity}"
            if product.is_unit:
                display_bilan += " pièces"
            else:
                display_bilan += "g"

        return display_bilan
