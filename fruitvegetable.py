class FruitVegetable:
    def __init__(self, name_fruit_vegetable: str, quantity: int, price: float,
                 is_unit: bool):
        """
        Definition of a fruitvegetable.

        :param str name_fruit_vegetable: name of the fruitvegetable
        :param int quantity: quantity - number of units / Number of Kilogram
        :param float price: price of the vegetable per unit, Example: Kilogram, unit
        :param bool is_unit: check if it is unit
        """
        self.name = name_fruit_vegetable
        self.quantity = quantity
        self.price = price
        self.is_unit = is_unit

    def __str__(self) -> str:
        """
        The str method is used to return a string representation of a fruitvegetable.

        :return: return a string representation of the fruitvegetable.
        """
        if self.is_out_of_stock():
            display_fruit_vegetable: str = f"{self.name}: Hors Stock\n"
        else:
            display_fruit_vegetable: str = f"{self.name}: {self.quantity}"

            if self.is_unit:
                display_fruit_vegetable += " pièces\n"
            else:
                display_fruit_vegetable += "g\n"

        return display_fruit_vegetable

    def price_remain_stock(self) -> float:
        """
        The total price of the remaining stock of the fruitvegetable
        :return: return the total price of the remaining stock of a fruitvegetable.
        """

        if self.is_unit:
            price_stock_remain_fruit_vegetable = self.quantity * self.price
        else:
            price_stock_remain_fruit_vegetable = self.quantity / 1000 * self.price

        return price_stock_remain_fruit_vegetable

    def is_out_of_stock(self) -> bool:
        """
        Return true if quantity is zero so out of stock
        :return: return True if the quantity is zero
        """
        return self.quantity == 0
        