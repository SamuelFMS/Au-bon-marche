from fruitvegetable import Fruitvegetable


class Command:
    basket: list[FruitAndVegetable]

    def __init__(self, basket: list[FruitAndVegetable] = []):
        self.basket = basket

    def __str__(self) -> str:
        if len(self.basket) == 0:
            return "Mon panier est vide"
        print("Panier : ")
        for b in self.basket:
            print(b)
