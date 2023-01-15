class Client:
    def __init__(self, id, nume, cnp, sold):
        self.id = id
        self.nume = nume
        self.cnp = cnp
        self.sold = sold

    def get_id_c(self):
        return self.id

    def get_nume(self):
        return self.nume

    def get_cnp(self):
        return self.cnp

    def get_sold(self):
        return self.sold

    def set_id_c(self,id):
        self.id = id

    def set_nume(self,nume):
        self.nume = nume

    def set_cnp(self, cnp):
        self.cnp = cnp

    def set_sold(self,sold):
        self.sold = sold

    def __str__(self):
        return f'Id Client: {self.id}, Nume Client: {self.nume}, Cnp Client: {self.cnp}, Sold Client: {self.sold}'
