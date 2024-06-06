from flask import request, jsonify
from models import load_json, save_json, Aluno, Curso
import os

data_dir = 'data'
alunos_file = os.path.join(data_dir, 'alunos.json')
cursos_file = os.path.join(data_dir, 'cursos.json')

def init_routes(app): 

    @app.route('/alunos', methods=['POST'])
    def create_aluno():
        data = request.get_json()
        alunos = load_json(alunos_file)
        novo_aluno = Aluno(id=len(alunos) + 1, nome=data['nome'], idade=data['idade'], curso_id=data['curso_id'])
        alunos.append(novo_aluno.to_dict())

        save_json(alunos_file, alunos)
        return jsonify({"message":"Aluno cadastrado com sucesso!"}), 201
    
    @app.route('/alunos', methods=['GET'])
    def get_alunos():
        alunos = load_json(alunos_file)
        return jsonify(alunos), 200
    

    @app.route('/cursos', methods=['POST'])
    def create_curso():
        data = request.get_json()
        cursos = load_json(cursos_file)
        novo_curso = Curso(id=len(cursos) + 1, nome=data['nome'])
        cursos.append(novo_curso.to_dict)

        save_json(cursos_file, cursos)
        return jsonify({"message":"Curso cadastrado com sucesso!"}), 201
    
    @app.route('/cursos', methods=['GET'])
    def get_cursos():
        cursos = load_json(cursos_file)
        return jsonify(cursos), 200