from fruitvegetable import FruitVegetable


class Command:
    basket: list[FruitVegetable]

    def __init__(self, basket: list[FruitVegetable] | None = None):
        if basket is None:
            basket = []
        self.basket = basket

    def __str__(self) -> str:
        if len(self.basket) == 0:
            return "Mon panier est vide"
        res: str = "Panier : \n"
        for b in self.basket:
            res += b.__str__()
        return res

    def add_to_basket(self, fruit_vegetable: FruitVegetable):
        self.basket.append(fruit_vegetable)
