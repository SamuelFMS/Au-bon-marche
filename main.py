from client import Client
from shop import Shop
def ask_yes_or_no(message: str):
    while True:
        saisie = input(message).upper()
        if saisie == "Y" or saisie == "YES":
            return True
        elif saisie == "N" or saisie == "NO":
            return False
        print("Entrez y ou n")

def main():
    shop: Shop = Shop()
    while True:
        if ask_yes_or_no("Voulez vous finir la journée: "):
            # Afficher le recupultatif de la journée
            Client.afficher_liste_clients()
            break
        else:
            # Creation d'un utilisateur
            new_client: Client = Client()
            new_client.register_user()
            while True:
                if ask_yes_or_no("Voulez vous ajouter un article au panier: "):
                    new_client.add_to_basket(shop)
                else:
                    break
        
  
    
if __name__ == '__main__':
    main()