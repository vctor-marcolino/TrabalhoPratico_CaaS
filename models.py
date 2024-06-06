import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save_json(file_path, data):
    with open(file_path, 'w') as file:
        return json.dump(data, file, indent=4)
    
class Aluno:
    def __init__(self, id, nome, idade, curso_id):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso_id = curso_id

    @staticmethod
    def from_dict(data):
        return Aluno(data['id'], data['nome'], data['idade'], data['curso_id'])

    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'curso_id': self.curso_id
        }
    
class Curso:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @staticmethod
    def from_dict(data):
        return Curso(data['id'], data['nome'])
    
    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome
        }