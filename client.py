from fruitvegetable import Fruitvegetable
from command import Command
from Shop import Shop
import copy


class Client:
    first_name: str
    last_name: str
    shop: Shop
    my_basket: Command

    def __init__(self, first_name: str, last_name: str, my_basket: Command = Command(), shop: Shop = Shop()):
        self.first_name = first_name
        self.last_name = last_name
        self.shop = shop
        self.my_basket = my_basket

    def add_to_basket(self):
        print(self.shop)
        res: Fruitvegetable = None
        while True:
            sass = input("Veuillez entrez le nom de l'article souhaitez: ")
            # Méthode a deplacer dans shop? return_article_in_shop(string)
            res = None
            for a in self.shop.product_list:
                if a.name == sass:
                    res = a
                    break

            if res is None:
                print("Nous avons pas réussis a trouver l'article souhaitez")
            else:
                break

        quantity: int = 0
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
