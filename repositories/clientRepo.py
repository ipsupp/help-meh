class ClientRepository:
    def __init__(self):
        self.clienti = {}

    def get_all_clienti(self):
        return list(self.clienti.values())

    def get_by_id_client(self, id):
        clienti = self.get_all_clienti()
        for client in clienti:
            if client.get_id_c() == id:
                return client

    def adauga_client(self, client):
        if self.get_by_id_client(client.get_id_c()) is not None:
            raise KeyError("Exista deja un client cu acest id!")
        self.clienti[client.get_id_c()] = client

    def modificare_client(self, clientNou):
        if self.get_by_id_client(clientNou.get_id_c()) is None:
            raise KeyError("Nu exista client cu acest id!")
        self.clienti[clientNou.get_id_c()] = clientNou

    def stergere_client(self, id):
        if self.get_by_id_client(id) is None:
            raise KeyError("Nu exista client cu acest id!")
        self.clienti.pop(id)

