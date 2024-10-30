import json


class CheckPerson:
    def __init__(self):
        self.cpf_cnpj: str
        self.estrutura_vendas: int
        self.source: str
        self.tipo_pessoa: str

    def _convert_params_person(self, data):
        person = CheckPerson()
        datas =  json.loads(data)


        person.cpf_cnpj = datas['cpf']
        person.estrutura_vendas = '1'
        person.source = 'TELEPORT'
        person.tipo_pessoa = 'fisica'

        if datas['typePerson'] == '2':
            person.tipo_pessoa = 'juridica'

        return person
