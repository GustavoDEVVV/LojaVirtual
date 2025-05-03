from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__, template_folder='../templates')
CORS(app)

# Alterando para salvar arquivos dentro de 'static/uploads'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Lista simulada de produtos
produtos = []

# Rota para servir imagens
@app.route('/uploads/<filename>')
def servir_imagem(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Rota principal - Página com os produtos
@app.route('/')
def index():
    return render_template('index.html')

# Rota para login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para painel administrativo
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Rota para editar produtos
@app.route('/editar')
def editar():
    return render_template('editar_produto.html')

# API - Listar produtos (GET)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# API - Adicionar produto (POST)
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
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
            'imagem': imagem.filename  # só o nome, mas você pode salvar o caminho também
        })
        return jsonify({'mensagem': 'Produto adicionado com sucesso!'}), 201

    else:
        novo_produto = request.get_json()
        produtos.append(novo_produto)
        return jsonify({'mensagem': 'Produto adicionado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
