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

    def __str__(self) -> str:
        """
        Create a method __str__ in order to display

        :return: Customer Personal Data
        """
        return (
            f"- Information Personelle -\n"
            f"Prénom: {self.first_name}\n"
            f"Nom: {self.last_name}\n"
            f"{self.my_basket}€\n"
        )

    @classmethod
    def afficher_liste_clients(cls):
        """
        Display information for each client
        """
        print("Liste des clients\nPrénom, NOM")
        for client in cls.clients:
            print(f"{client.first_name.capitalize()}, {client.last_name.upper()}")

    @classmethod
    def get_price_total(cls) -> float:
        """
        Calculation of the total price of the basket for each client
        :param List client cls: is a list of clients
        :return: total price for each client
        """
        total = 0
        for client in cls.clients:
            total += client.my_basket.price_of_basket()
        return round(total, 2)

    def register_user(self):
        """
        Save client information
        """
        self.first_name = input("Veuillez entrez le prenom: ")
        self.last_name = input("Veuillez entrez le nom: ")

    def add_to_basket(self, shop: Shop) -> Shop:
        """
        Add a fruit or a vegetable to the basket
        :param shop: a list of products that includes fruits and vegetables
        :return: a shop object
        """
        print(shop)
        while True:
            name_article = input("Veuillez entrez le nom de l'article souhaitez: ")

            if name_article in shop.get_list_name():
                index_fruit_vegetable: int = shop.get_list_name().index(name_article)
                res: FruitVegetable = shop.product_list[index_fruit_vegetable]

                if not res.is_out_of_stock():
                    break
                print("Nous n'en avons plus en magasin.")

            print("Nous avons pas réussis a trouver l'article souhaitez.")

        quantity_in_shop = res.quantity

        while True:
            quantity = input(f"Veuillez saisir la quantité({"unit" if res.is_unit else "g"}): ")

            if quantity.isdigit():
                quantity = int(quantity)
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
        """
        :return: boolean that check if the client has finished the command
        """
        while True:
            input_user = input("Est-ce que vous continuez votre commande ? [Y/n]")
            if input_user.lower() == 'y' or input_user == '':
                return False
            if input_user == 'n':
                return True
