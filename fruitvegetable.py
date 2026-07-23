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
        return self.name + ", " + str(self.quantity) + ", " + str(self.price) + ", " + str(self.is_unit)
