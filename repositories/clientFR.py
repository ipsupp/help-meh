from domain.client import Client
from repositories.clientRepo import ClientRepository


class ClientFR(ClientRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, client):
        super().adauga_client(client)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:

                id = line.split()[0]
                nume = line.split()[1]
                cnp = line.split()[2]
                sold = line.split()[3]

                client = Client(id, nume, cnp, sold)
                self.clienti[id] = client

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for client in self.get_all_clienti():
                f.write(f'{client.get_id_c()},{client.get_nume()},{client.get_cnp()},{client.get_sold()}\n')


