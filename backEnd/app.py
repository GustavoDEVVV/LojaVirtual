from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='../templates')
CORS(app)

# Lista simulada de produtos
produtos = []

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
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify({'mensagem': 'Produto adicionado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
