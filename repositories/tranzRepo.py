from repositories.clientRepo import ClientRepository


class TranzRepository:
    def __init__(self, clientRepository: ClientRepository):
        super().__init__()
        self.tranzactii = {}
        self.clientRepository = clientRepository

    def get_all_tranz(self):
        return list(self.tranzactii.values())

    def get_by_id(self,id):
        tranz = self.get_all_tranz()
        for a in tranz:
            if a.get_id_c() == id:
                return a

    def adauga_tranz(self, tranz):
        if tranz.get_id_c() is not None:
            raise KeyError("Exista deja tranzactie cu id-ul dat!")
        if tranz.get_idcs() is None:
            raise KeyError("Nu exista clientul sursa!")
        if tranz.get_idcd() is None:
            raise KeyError("Nu exista clientul destinatar!")
        if tranz.get_idcd() == tranz.get_idcs():
            raise KeyError("Clientul sursa nu poate fi clientul destinatar!")
        self.tranzactii[tranz.get_id_c] = tranz
        



