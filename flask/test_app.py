import unittest
import json
from app import app, db, Aluno

class TestAlunoAPI(unittest.TestCase):

    def setUp(self):
        # Configuração do ambiente de teste
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória para testes
        self.client = app.test_client()

        with app.app_context():
            db.create_all()  # Criação das tabelas no ambiente de teste

    def tearDown(self):
        # Limpar o banco após cada teste
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_adicionar_aluno_sucesso(self):
        # Dados do aluno a ser cadastrado
        payload = {
            "nome": "Carlos",
            "sobrenome": "Silva",
            "turma": "1A",
            "disciplinas": "Matemática, Física"
        }

        # Realiza a requisição para adicionar aluno
        response = self.client.post('/alunos', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Aluno adicionado com sucesso!', response.json['message'])

        # Verifica se o aluno foi inserido no banco
        with app.app_context():
            aluno = Aluno.query.filter_by(nome="Carlos", sobrenome="Silva").first()
            self.assertIsNotNone(aluno)
            self.assertEqual(aluno.turma, "1A")
            self.assertEqual(aluno.disciplinas, "Matemática, Física")

    def test_adicionar_aluno_campos_obrigatorios(self):
        # Dados do aluno sem alguns campos obrigatórios
        payload = {
            "nome": "Carlos",
            "sobrenome": "Silva",
            # Faltando turma e disciplinas
        }

        # Realiza a requisição para adicionar aluno
        response = self.client.post('/alunos', data=json.dumps(payload), content_type='application/json')

        # Verifica se a resposta é de erro (400) e se a mensagem de erro é adequada
        self.assertEqual(response.status_code, 400)
        self.assertIn('Campo turma é obrigatório!', response.json['message'])

    def test_listar_alunos(self):
        # Adiciona alguns alunos no banco
        with app.app_context():
            db.session.add(Aluno(nome="Carlos", sobrenome="Silva", turma="1A", disciplinas="Matemática"))
            db.session.add(Aluno(nome="Ana", sobrenome="Souza", turma="2B", disciplinas="Português, História"))
            db.session.commit()

        # Realiza a requisição para listar alunos
        response = self.client.get('/alunos')
        self.assertEqual(response.status_code, 200)
        alunos = response.json
        self.assertEqual(len(alunos), 2)
        self.assertEqual(alunos[0]['nome'], "Carlos")
        self.assertEqual(alunos[1]['nome'], "Ana")

if __name__ == '__main__':
    unittest.main()
