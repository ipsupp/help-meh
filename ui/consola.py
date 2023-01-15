from repositories.clientRepo import ClientRepository
from repositories.tranzRepo import TranzRepository
from service.Service import Service


class Console:
    def __init__(self, service: Service):
        self.service = service

    def afisare_c(self, clienti):
        for a in clienti:
            print(a)

    def afisare_t(self, tranzactii):
        for a in tranzactii:
            print(a)

    def adauga_c(self):
        try:
            id = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            cnp = input("Dati cnp-ul clientului: ")
            sold = int(input("Dati soldul clientului: "))
            self.service.adauga_c(id,nume,cnp,sold)
        except KeyError as e:
            print (e)
        clienti = self.service.get_all_c()
        self.afisare_c(clienti)

    def adauga_t(self):
        try:
            id = input("Dati id-ul tranzactiei: ")
            id_cs = input("Dati id-ul clientului sursa: ")
            id_cd = input("Dati id-ul clientului destinatie: ")
            value = input("Dati valoarea tranzactiei: ")
            self.service.adauga_t(id, id_cs, id_cd, value)
        except KeyError as e:
            print (e)
        tranzactii = self.service.get_all_t()
        self.afisare_t(tranzactii)

    def ui_meniu(self):
        print("1. Adauga client")
        print("2. Adauga tranzactie")
        print("x. Inchidere program")

    def Meniu(self):
        while True:
            self.ui_meniu()
            option = input("Alegeti optiunea: ")
            if option == "1":
                self.adauga_c()
            if option == "2":
                self.adauga_t()
            if option == "x":
                break

