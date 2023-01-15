class Tranzactie:
    def __init__(self, id, id_cs, id_cd, value):
        self.id = id
        self.id_cs = id_cs
        self.id_cd = id_cd
        self.value = value

    def get_id_c(self):
        return self.id

    def get_id_cs(self):
        return self.id_cs

    def get_id_cd(self):
        return self.id_cd

    def get_value(self):
        return self.value

    def set_id(self, id):
        self.id = id

    def set_id_cs(self, id_cs):
        self.id_cs = id_cs

    def set_id_cd(self, id_cd):
        self.id_cd = id_cd

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return f'Id Tranzactie: {self.id}, Id Client-Sursa: {self.id_cs}, Id Client-Destinatie: {self.id_cd}, Valoare: {self.value}'
    