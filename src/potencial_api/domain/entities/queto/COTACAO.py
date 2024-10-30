from potencial_api.domain.entities.queto.CONDUTORP import CONDUTORP
from potencial_api.domain.entities.queto.PROPRIETARIO import PROPRIETARIO
from potencial_api.domain.entities.queto.SEGURADO import SEGURADO
from potencial_api.domain.entities.queto.VEICULO import VEICULO


class COTACAO:
    def __init__(self):
        self.TIPOSEG = ""
        self.SEGURADO = SEGURADO()
        self.PROPRIETARIO = PROPRIETARIO()
        self.CONDUTORP = CONDUTORP()
        self.VEICULO = VEICULO()