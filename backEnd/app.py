from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

# Pasta onde as imagens serão salvas
UPLOAD_FOLDER = os.path.join('static', 'imagens')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Simulando banco de dados
produtos = []
id_produto = 1

# Rota inicial: login
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/editar')
def editar():
    return render_template('editar.html', produtos=produtos)

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    global id_produto

    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    imagem = request.files.get('imagem')

    if not nome or not descricao or not imagem:
        return jsonify({'mensagem': 'Todos os campos são obrigatórios.'}), 400

    filename = secure_filename(imagem.filename)
    imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    produtos.append({
        'id': id_produto,
        'nome': nome,
        'descricao': descricao,
        'imagem': filename
    })
    id_produto += 1

    return jsonify({'mensagem': 'Produto adicionado com sucesso!'})

@app.route('/produtos/<int:id>', methods=['POST'])
def atualizar_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return jsonify({'mensagem': 'Produto não encontrado'}), 404

    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    imagem = request.files.get('imagem')

    if nome:
        produto['nome'] = nome
    if descricao:
        produto['descricao'] = descricao
    if imagem:
        filename = secure_filename(imagem.filename)
        imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        produto['imagem'] = filename

    return jsonify({'mensagem': 'Produto atualizado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
