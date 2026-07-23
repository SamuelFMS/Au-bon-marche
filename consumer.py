from client import Client


class consumer:
    clients: list[Client]

    def __init__(self, clients: list[Client] = []):
        self.clients = clients
