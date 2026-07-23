from client import Client


class Consumer:
    clients: list[Client]

    def __init__(self, clients: list[Client] = []):
        self.clients = clients

    def __str__(self):  
        res: str = "Liste des clients\nPrénom, NOM\n"
        for client in self.clients:
            res += f"{client.first_name.capitalize()}, {client.last_name.upper()} \n"
        return res
    
    def add_client(self, client):
        self.clients.append(client)
