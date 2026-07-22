from fruitvegetable import Fruitvegetable


class Command:
    basket: list[Fruitvegetable]

    def __init__(self, basket: list[Fruitvegetable] = []):
        self.basket = basket

    def __str__(self) -> str:
        if len(self.basket) == 0:
            return "Mon panier est vide"
        res: str = "Panier : \n"
        for b in self.basket:
            res+= f"{b}"
        return res
