from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for, session
import os
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')

app.secret_key = 'segredo-seguro'  # Necessário para sessões
CORS(app)

# Pasta de upload
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Banco simulado de usuários
usuarios = {
    'admin@site.com': {'senha': 'admin123', 'tipo': 'admin'},
    'usuario@site.com': {'senha': 'user123', 'tipo': 'usuario'}
}

# Lista simulada de produtos
produtos = []

# Rota para servir imagens
@app.route('/uploads/<filename>')
def servir_imagem(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Página inicial
@app.route('/')
def index():
    if session.get('tipo') != 'usuario':
        return redirect(url_for('login'))
    return render_template('index.html')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = usuarios.get(email)

        if user and user['senha'] == senha:
            session['usuario'] = email
            session['tipo'] = user['tipo']
            return redirect(url_for('admin' if user['tipo'] == 'admin' else 'index'))
        else:
            return render_template('login.html', erro='Credenciais inválidas')
    return render_template('login.html')

# Painel admin
@app.route('/admin')
def admin():
    if session.get('tipo') != 'admin':
        return redirect(url_for('login'))
    return render_template('PaginaDaAdmin.html')

# Criação de produtos
@app.route('/criar')
def criacao_de_produtos():
    return render_template('CriacaoDeProdutos.html')

# Página de edição de produtos
@app.route('/editar')
def editar():
    if session.get('tipo') != 'admin':
        return redirect(url_for('login'))
    return render_template('editar_produto.html', produtos=produtos)

# Editar um produto específico
@app.route('/editar_produto/<int:index>', methods=['POST'])
def editar_produto(index):
    if session.get('tipo') != 'admin':
        return redirect(url_for('login'))
    if 0 <= index < len(produtos):
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        produtos[index]['nome'] = nome or produtos[index]['nome']
        produtos[index]['descricao'] = descricao or produtos[index]['descricao']
    return redirect(url_for('editar'))

# Excluir produto
@app.route('/excluir_produto/<int:index>', methods=['POST'])
def excluir_produto(index):
    if session.get('tipo') != 'admin':
        return redirect(url_for('login'))
    if 0 <= index < len(produtos):
        produtos.pop(index)
    return redirect(url_for('editar'))

# API - listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# API - adicionar produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    if session.get('tipo') != 'admin':
        return redirect(url_for('login'))
    if request.content_type.startswith('multipart/form-data'):
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')

        if not nome or not descricao or not imagem:
            return jsonify({'mensagem': 'Todos os campos são obrigatórios!'}), 400

        caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], imagem.filename)
        imagem.save(caminho_imagem)

        produtos.append({
            'nome': nome,
            'descricao': descricao,
            'imagem': imagem.filename
        })
        return jsonify({'mensagem': 'Produto adicionado com sucesso!'}), 201
    else:
        novo_produto = request.get_json()
        produtos.append(novo_produto)
        return jsonify({'mensagem': 'Produto adicionado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
