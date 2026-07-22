from fruit_and_vegetable import Fruit_And_Vegetable
from command import Command

class Client:
    first_name: str
    last_name: str
    list_fruit_vegetable: list[Fruit_And_Vegetable]
    my_basket : Command 
    
    def __init__(self, first_name: str, last_name: str, list_fruit_vegetable:list[Fruit_And_Vegetable]=[], my_basket:Command=Command()):
        self.first_name = first_name
        self.last_name = last_name
        self.list_fruit_vegetable = list_fruit_vegetable
        self.my_basket = my_basket
