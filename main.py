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
    """
    Main function:
    1) Create the shop
    2) Create the customer
    3) Process the customer’s orders in the shop
    4) Display a summary of the customer’s orders once they have been completed
    5) Return to step 2 if it's not the end of the day or if the shop isn't out of stock
    6) Display all customers and the shop’s daily till balance
    """
    shop: Shop = Shop()

    while True:
        # Create a client
        customer: Client = Client()
        customer.register_user()

        # Create command to a new client
        shop = customer.select_fruit_and_vegetable_to_add_to_basket(shop)

        while not customer.end_command():
            if shop.is_fruits_vegetables_out_of_stock():
                print("Notre boutique a été dévalisé. Fin de la commande.")
                break
            shop = customer.select_fruit_and_vegetable_to_add_to_basket(shop)

        print(customer)
        if shop.is_fruits_vegetables_out_of_stock() or ask_yes_or_no("Voulez-vous finir la journée [y/yes/n/no]: "):
            # Afficher le récapitulatif de la journée
            print("-" * 60)
            Client.afficher_liste_clients()
            print(f"Recette de la journée: {Client.get_price_total()}€")
            break

    print(shop)


if __name__ == '__main__':
    main()
