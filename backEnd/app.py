from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

# Modelo de Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.String(100), nullable=False)

# Rota para a página principal (exibe os produtos)
@app.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)

# Rota para login (simples para exemplo)
@app.route('/login')
def login():
    return render_template('login.html')

# Painel Administrativo
@app.route('/admin')
def admin():
    produtos = Produto.query.all()
    return render_template('admin.html', produtos=produtos)

# Página para adicionar um novo produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        imagem = request.files['imagem']

        if imagem:
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], imagem.filename)
            imagem.save(caminho_imagem)

            novo_produto = Produto(nome=nome, descricao=descricao, imagem=imagem.filename)
            db.session.add(novo_produto)
            db.session.commit()

            return redirect(url_for('admin'))
    return render_template('adicionar_produto.html')

# Página para editar produto
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']

        imagem = request.files['imagem']
        if imagem:
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], imagem.filename)
            imagem.save(caminho_imagem)
            produto.imagem = imagem.filename

        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('editar_produto.html', produto=produto)

# Rota para excluir produto
@app.route('/excluir/<int:id>')
def excluir(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('admin'))

# Função para rodar o app
if __name__ == '__main__':
    # Cria o banco de dados e as tabelas se ainda não existirem
    with app.app_context():
        db.create_all()

    app.run(debug=True)
