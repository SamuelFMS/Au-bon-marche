from typing import ClassVar

from fruitvegetable import FruitVegetable
from command import Command
from shop import Shop

import copy


class Client:
    clients: ClassVar[list[Client]] = []

    def __post_init__(self):
        Client.clients.append(self)

    def __init__(self):
        self.first_name: str = ""
        self.last_name: str = ""
        self.my_basket: Command = Command()
        Client.clients.append(self)

    def __str__(self):
        return (
            f"- Information Personelle -\n"
            f"Prénom: {self.first_name}\n"
            f"Nom: {self.last_name}\n"
            f"{self.my_basket}\n"
        )

    @classmethod
    def afficher_liste_clients(cls):
        print("Liste des clients\nPrénom, NOM")
        for client in cls.clients:
            print(f"{client.first_name.capitalize()}, {client.last_name.upper()}")
            
    @classmethod
    def get_price_total(cls):
        total = 0
        for client in cls.clients:
            total += client.my_basket.price_of_basket()
        return total
    
    def register_user(self):
        self.first_name = input("Veuillez entrez le prenom: ")
        self.last_name = input("Veuillez entrez le nom: ")

    def add_to_basket(self, shop: Shop) -> Shop:
        print(shop)
        while True:
            sass = input("Veuillez entrez le nom de l'article souhaitez: ")

            if sass in shop.get_list_name():
                break
            print("Nous avons pas réussis a trouver l'article souhaitez")

        index_fruit_vegetable: int = shop.get_list_name().index(sass)
        res: FruitVegetable = shop.product_list[index_fruit_vegetable]
        quantity: int

        while True:
            sass = input(f"Veuillez saisir la quantité({"unit" if res.is_unit else "g"}): ")

            if sass.isdigit():
                quantity = int(sass)
                if 0 < quantity <= res.quantity:
                    break
                print("Nous avons plus assez dans le stock")
            else:
                print("Veuillez entrez un nombre valide")

        self.my_basket.add_to_basket(copy.copy(res))
        shop.product_list[index_fruit_vegetable].quantity -= quantity

        return shop

    @staticmethod
    def end_command():
        while True:
            input_user = input("Est-ce que vous continuez votre commande ? [Y/n]")
            if input_user.lower() == 'y' or input_user == '':
                return False
            if input_user == 'n':
                return True
