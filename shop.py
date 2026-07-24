from fruitvegetable import FruitVegetable


class Shop:
    product_list: list[FruitVegetable]

    def __init__(self, product_list=None):
        """
        Create a list of products that includes fruits and vegetables

        :param product_list: List of fruits and vegetables
        """
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
        """
        Display all the fruit and vegetables available in-store, along with the number of each item in stock.

        :return: Display balance sheet in the shop
        """
        display_balance_sheet: str = f"Nombre de fruit et de légumes restants: {str(self.nb_fruit_vegetable())}.\n"
        display_balance_sheet += "Voici le stock disponible:\n"

        for product in self.product_list:
            display_balance_sheet += product.__str__()

        return display_balance_sheet

    def nb_fruit_vegetable(self) -> int:
        """
        Number of fruits and vegetables

        :return: Number of fruits and vegetables
        """
        return len([product for product in self.product_list if not product.is_out_of_stock()])

    def get_list_name(self) -> list[str]:
        """
        Retrieve all the names of fruits and vegetables on the list

        :return: Names of fruits and vegetables
        """
        return [fruit_vegetable.name for fruit_vegetable in self.product_list]
