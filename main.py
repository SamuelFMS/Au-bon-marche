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
        # Création d'un utilisateur
        new_client: Client = Client()
        new_client.register_user()
        shop = new_client.select_fruit_and_vegetable_to_add_to_basket(shop)

        while True:
            if new_client.end_command():
                break
            shop = new_client.select_fruit_and_vegetable_to_add_to_basket(shop)

        while not customer.end_command():
            shop = customer.select_fruit_and_vegetable_to_add_to_basket(shop)

        print(customer)
        if ask_yes_or_no("Voulez-vous finir la journée [y/yes/n/no]: "):
            # Afficher le récapitulatif de la journée
            print("-" * 60)
            Client.afficher_liste_clients()
            print(f"Recette de la journée: {Client.get_price_total()}€")
            break

    print(shop)


if __name__ == '__main__':
    main()
