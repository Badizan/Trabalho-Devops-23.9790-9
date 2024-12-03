from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    turma = db.Column(db.String(10), nullable=False)
    disciplinas = db.Column(db.String(200), nullable=False)

@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.get_json()

    # Verifica se todos os campos obrigatórios estão presentes
    required_fields = ['nome', 'sobrenome', 'turma', 'disciplinas']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Campo {field} é obrigatório!'}), 400

    novo_aluno = Aluno(
        nome=data['nome'],
        sobrenome=data['sobrenome'],
        turma=data['turma'],
        disciplinas=data['disciplinas']
    )

    db.session.add(novo_aluno)
    db.session.commit()

    return jsonify({'message': 'Aluno adicionado com sucesso!'}), 201

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    alunos_list = [{'nome': aluno.nome, 'sobrenome': aluno.sobrenome, 'turma': aluno.turma, 'disciplinas': aluno.disciplinas} for aluno in alunos]
    return jsonify(alunos_list)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
