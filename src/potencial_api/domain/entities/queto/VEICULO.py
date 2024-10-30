from potencial_api.domain.entities.queto.PERFILUSOVEIC import PERFILUSOVEIC


class VEICULO:
    def __init__(self):
        self.CODCAR = ""
        self.MARCA = ""
        self.ANOFABR = ""
        self.ANOMODELO = ""
        self.COMBUSTIVEL = ""
        self.CATEG = None
        self.ZEROKM = ""
        self.UTILIZACAO = None
        self.PERFILUSOVEIC = PERFILUSOVEIC()
        self.CEPPERNOITE = ""
        self.CEPCIRC = ""
        self.CEPPRESID = ""
        self.PLACANUM = ""
        self.CAMBIOAUTO = ""