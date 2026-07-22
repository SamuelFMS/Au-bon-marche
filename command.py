from fruit_and_vegetable import Fruit_And_Vegetable

class Command:
    basket: list[Fruit_And_Vegetable] 
    
    def __init__(self, basket: list[Fruit_And_Vegetable] = []):
        self.basket = basket
        
    def __str__(self) -> str:
        if len(self.basket) == 0:
            return "Mon panier est vide"
        print("Panier : ")
        for b in self.basket:
            print(b)
