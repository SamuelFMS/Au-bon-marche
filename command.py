from fruit_and_vegetable import Fruit_And_Vegetable

class Command:
    basket: list[Fruit_And_Vegetable] 
    
    def __init__(self, basket = []):
        self.basket = basket