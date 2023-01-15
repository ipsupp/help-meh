from repositories.clientFR import ClientFR
from repositories.clientRepo import ClientRepository
from repositories.tranzFR import TranzFR
from service.Service import Service
from ui.consola import Console


def main():

    clientRepository = ClientFR("C.txt")
    tranzRepository = TranzFR("T.txt", clientRepository)

    service = Service(clientRepository, tranzRepository)
    consola = Console(service)
    consola.Meniu()

main()