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
        res += f"Total de la commande: {self.price_of_basket()}"
        return res

    def price_of_basket(self):
        price = 0
        for fv in self.basket:
            if fv.is_unit:
                price += fv.price * fv.quantity
            else:
                price += fv.price / 1000 * fv.quantity
        return round(price, 2)

    def add_to_basket(self, fruit_vegetable: FruitVegetable):
        self.basket.append(fruit_vegetable)
