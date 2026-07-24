from fruitvegetable import FruitVegetable


class Command:
    basket: list[FruitVegetable]

    def __init__(self, basket: list[FruitVegetable] | None = None):
        """
        Take all Fruits and Vegetables by customer.

        :param basket: Basket of customer.
        """
        if basket is None:
            basket = []
        self.basket = basket

    def __str__(self) -> str:
        """
        Display the customer’s shopping basket, showing the total amount.

        :return: Basket summary
        """
        if len(self.basket) == 0:
            return "Mon panier est vide"

        res: str = "Panier : \n"
        for fruit_vegetable in self.basket:
            res += fruit_vegetable.__str__()

        res += f"Total de la commande: {self.price_of_basket()}"
        return res

    def price_of_basket(self) -> float:
        """
        Calculate the total amount of the customer's order.

        :return: Total amount of the basket.
        """
        price = 0
        for fruit_vegetable in self.basket:
            price += fruit_vegetable.price_remain_stock()
        return round(price, 2)

    def add_to_basket(self, fruit_vegetable: FruitVegetable):
        """
        Add a fruit or a vegetable to a basket.

        :param fruit_vegetable: The fruit or vegetable to add
        """
        self.basket.append(fruit_vegetable)
