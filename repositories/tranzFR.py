from domain.tranzactie import Tranzactie
from repositories.clientRepo import ClientRepository
from repositories.tranzRepo import TranzRepository


class TranzFR(TranzRepository):
    def __init__(self, fileName, clientFileRepository):
        super().__init__(clientFileRepository)
        self.fileName = fileName
        self.__readFile()

    def adauga(self,tranz):
        super().adauga_tranz(tranz)
        self.__writeFile()

    def __writeFile(self):
        with open(self.fileName, 'w') as f:
            for obiect in self.get_all():
                f.write(f'{obiect.get_id_c()} {obiect.get_idcs()} {obiect.get_idcd()} {obiect.get_value()} \n ')

    def __readFile(self):
        with open(self.fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                id = line.split()[0]
                id_cs = line.split()[1]
                id_cd = line.split()[2]
                value = line.split()[3]

                tranzactie = Tranzactie(id, id_cs, id_cd, value)
                super().adauga_tranz(tranzactie)

            f.close()

