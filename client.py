from fruitvegetable import Fruitvegetable
from command import Command

class Client:
    first_name: str
    last_name: str
    list_fruit_vegetable: list[Fruitvegetable]
    my_basket : Command 
    
    def __init__(self, first_name: str, last_name: str, list_fruit_vegetable:list[Fruitvegetable]=[], my_basket:Command=Command()):
        self.first_name = first_name
        self.last_name = last_name
        self.list_fruit_vegetable = list_fruit_vegetable
        self.my_basket = my_basket
    
    def __str__(self):
        return (
            f"- Information Personelle -\n"
            f"Prénom: {self.first_name}\n"
            f"Nom: {self.last_name}\n"
            f"{self.my_basket}"
            )
