class ProdutoDB:
    def __init__(self):
        # Simulando banco de dados em memória
        self.produtos = []
        self.proximo_id = 1

    def listar(self):
        return self.produtos

    def adicionar(self, nome, descricao, imagem):
        produto = {
            'id': self.proximo_id,
            'nome': nome,
            'descricao': descricao,
            'imagem': imagem
        }
        self.produtos.append(produto)
        self.proximo_id += 1

    def buscar(self, id):
        for produto in self.produtos:
            if produto['id'] == id:
                return produto
        return None

    def editar(self, id, nome, descricao, imagem):
        produto = self.buscar(id)
        if produto:
            produto['nome'] = nome
            produto['descricao'] = descricao
            produto['imagem'] = imagem

    def excluir(self, id):
        self.produtos = [p for p in self.produtos if p['id'] != id]
