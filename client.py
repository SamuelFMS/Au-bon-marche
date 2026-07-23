import shop
from fruitvegetable import FruitVegetable
from command import Command
from shop import Shop
import copy


class Client:
    def __init__(self):
        self.first_name: str = ""
        self.last_name: str = ""
        self.my_basket: Command = Command()

    def __init__(self, first_name: str, last_name: str, my_basket: Command = Command(), shop: Shop = Shop()):
        self.first_name = first_name
        self.last_name = last_name
        self.shop = shop
        self.my_basket = my_basket

    @staticmethod
    def register_user() -> Client:
        first_name = input("Veuillez entrez le prenom: ")
        last_name = input("Veuillez entrez le nom: ")
        return Client(first_name, last_name)

    def add_to_basket(self):
        print(self.shop)
        while True:
            sass = input("Veuillez entrez le nom de l'article souhaitez: ")
            # Méthode a deplacer dans shop? return_article_in_shop(string)
            if sass in self.shop.get_list_name():
                break
            print("Nous avons pas réussis a trouver l'article souhaitez")

        res: FruitVegetable = self.shop.product_list[self.shop.get_list_name().index(sass)]

        quantity: int
        while True:
            sass = input(f"Veuillez saisir la quantité({"unit" if res.is_unit else "g"}): ")
            if sass.isdigit():
                quantity = int(sass)
                if quantity <= res.quantity:
                    break
                else:
                    print("Nous avons plus assez dans le stock")
            else:
                print("Veuillez entrez un nombre valide")

        if quantity != 0:
            copy_fruit_vegetable = copy.copy(res)
            copy_fruit_vegetable.quantity = quantity
            res.quantity -= quantity
            self.my_basket.add_to_basket(copy_fruit_vegetable)

    def __str__(self):
        return (
            f"- Information Personelle -\n"
            f"Prénom: {self.first_name}\n"
            f"Nom: {self.last_name}\n"
            f"{self.my_basket}"
        )
