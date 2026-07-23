from fruitvegetable import FruitVegetable
from command import Command
from shop import Shop


class Client:
    def __init__(self):
        self.first_name: str = ""
        self.last_name: str = ""
        self.my_basket: Command = Command()

    def __str__(self):
        return (
            f"- Information Personelle -\n"
            f"Prénom: {self.first_name}\n"
            f"Nom: {self.last_name}\n"
            f"{self.my_basket}\n"
            f"{self.my_basket.price_of_basket()}"
        )

    @classmethod
    def register_user(cls):
        cls.first_name = input("Veuillez entrez le prenom: ")
        cls.last_name = input("Veuillez entrez le nom: ")

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

        self.my_basket.add_to_basket(res)
        shop.product_list[index_fruit_vegetable].quantity -= quantity

        return shop
