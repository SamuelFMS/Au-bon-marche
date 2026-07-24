from copy import copy
from typing import ClassVar

from fruitvegetable import FruitVegetable
from command import Command
from shop import Shop


class Client:  # Create a Client class.

    clients: ClassVar[list[Client]] = []  # The variable clients is a list of client.

    def __init__(self):
        """
        Initialize first_name, last_name and my_basket.
        """
        self.first_name: str = ""
        self.last_name: str = ""
        self.my_basket: Command = Command()
        Client.clients.append(self)

    def __str__(self) -> str:  # Create a method __str__ in order to display
        return (
            f"- Information Personelle -\n"
            f"Prénom: {self.first_name.capitalize()}\n"
            f"Nom: {self.last_name.upper()}\n"
            f"{self.my_basket}€\n"
        )

    @classmethod
    def afficher_liste_clients(cls):
        print("Liste des clients\nPrénom, NOM")
        for client in cls.clients:
            print(f"{client.first_name.capitalize()}, {client.last_name.upper()}")

    @classmethod
    def get_price_total(cls) -> float:
        total = 0
        for client in cls.clients:
            total += client.my_basket.price_of_basket()
        return round(total, 2)

    def register_user(self):
        self.first_name = input("Veuillez entrez le prenom: ")
        self.last_name = input("Veuillez entrez le nom: ")

    def select_fruit_and_vegetable_to_add_to_basket(self, shop: Shop) -> Shop:
        print(shop)
        while True:
            sass = input("Veuillez entrez le nom de l'article souhaitez: ")

            if sass in shop.get_list_name():
                index_fruit_vegetable: int = shop.get_list_name().index(sass)
                res: FruitVegetable = shop.product_list[index_fruit_vegetable]

                if not res.is_out_of_stock():
                    break
                print("Nous n'en avons plus en magasin.")

            print("Nous avons pas réussis a trouver l'article souhaitez.")

        quantity_in_shop = res.quantity
        quantity: int

        while True:
            sass = input(f"Veuillez saisir la quantité({"unit" if res.is_unit else "g"}): ")

            if sass.isdigit():
                quantity = int(sass)
                if 0 < quantity <= res.quantity:
                    res.quantity = quantity
                    break
                print("Nous avons plus assez dans le stock")
            else:
                print("Veuillez entrez un nombre valide")

        self.my_basket.add_to_basket(copy(res))
        shop.product_list[index_fruit_vegetable].quantity = quantity_in_shop - quantity

        return shop

    @staticmethod
    def end_command() -> bool:
        while True:
            input_user = input("Est-ce que vous continuez votre commande ? [Y/n]")
            if input_user.lower() == 'y' or input_user == '':
                return False
            if input_user == 'n':
                return True
