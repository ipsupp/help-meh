from domain.client import Client
from domain.tranzactie import Tranzactie
from repositories.clientRepo import ClientRepository
from repositories.tranzRepo import TranzRepository


class Service:
    def __init__(self, clientRepository: ClientRepository, tranzRepository: TranzRepository):
        self.clientRepository = clientRepository
        self.tranzRepository = tranzRepository

    def get_all_c(self):
        return self.clientRepository.get_all_clienti()

    def get_all_t(self):
        return self.tranzRepository.get_all_tranz()

    def adauga_c(self, id, nume, cnp, sold):
        client = Client(id, nume, cnp, sold)
        self.clientRepository.adauga_client(client)

    def adauga_t(self, id, id_cs, id_cd, value):
        tranz = Tranzactie(id, id_cs, id_cd, value)
        self.tranzRepository.adauga_tranz(tranz)
        client_sursa = self.clientRepository.get_by_id_client(id_cs)
        client_destinatie = self.clientRepository.get_by_id_client(id_cd)
        cs_sold = int(client_sursa.get_sold() - value)
        cd_sold = int(client_destinatie.get_sold() + value)
        client_sursa.set_sold(cs_sold)
        client_destinatie.set_sold(cd_sold)
        self.clientRepository.modificare_client(client_sursa)
        self.clientRepository.modificare_client(client_destinatie)




