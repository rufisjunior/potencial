
class PersonModel:
    def __init__(self):
        self.nome: str
        self.cpf: str
        self.data_nascimento: str

    def _convert(self, person_data):
        person = PersonModel()

        if person_data is None:
            return person
        
        person.nome = person_data['nome']
        person.cpf = person_data['cpf']
        person.data_nascimento = person_data['data_nascimento']

        return person