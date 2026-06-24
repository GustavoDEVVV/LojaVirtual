# Nexora

Loja virtual simples com painel de administração, desenvolvida com Python e Flask.

---

## Descrição

O Nexora é uma loja virtual com sistema de login e controle de permissões entre dois tipos de usuário: administradores, que podem cadastrar, editar e remover produtos, e usuários comuns, que apenas visualizam o catálogo disponível. O projeto separa claramente frontend (interface) e backend (lógica de negócio), e foi criado como uma forma prática de aplicar conceitos de desenvolvimento web full stack com deploy real em produção.

---

## Demonstração

**Aplicação online:**
- Site: *https://lojavirtual-u4pn.onrender.com/*
- Repositório: *https://github.com/GustavoDEVVV/LojaVirtual*

---

## Tecnologias

### Back-end
- Python
- Flask

### Front-end
- HTML5
- CSS3
- JavaScript

### Banco de Dados
- Arquivo JSON (`banco_produtos.json`)
- SQLite (`database.db`)
- Models (`produto.py`)

### Infraestrutura
- Git / GitHub
- Render (deploy)
- Gunicorn (servidor WSGI de produção)

---

## Arquitetura

```
Usuário
  ↓
Frontend (HTML / CSS / JS)
  ↓
Flask (app.py)
  ↓
Banco de Dados (JSON / SQLite)
```

---

## Estrutura de Pastas

```
LOJAVIRTUAL/
│
├── .gitattributes
├── README.md
├── app.py
├── Procfile
├── requirements.txt
│
├── backEnd/
│   ├── database/
│   ├── instance/
│   ├── models/
│   ├── static/
│   ├── database.db
│   └── uploads/
│       └── banco_produtos.json
│
├── static/
│   ├── css/
│   │   ├── CriacaoDeProdutos.css
│   │   ├── editar_produto.css
│   │   ├── index.css
│   │   ├── login.css
│   │   ├── pagina_da_admin.css
│   │   ├── ResponsividadeMobile.css
│   │   └── ResponsividadeMobilePaginasIguais.css
│   │
│   ├── imagens/
│   │   ├── criacaoDeProdutos/
│   │   ├── index/
│   │   ├── login/
│   │   ├── PaginaAdministracao/
│   │   └── Favicon.png
│   │
│   └── uploads/
│
└── templates/
    ├── CriacaoDeProdutos.html
    ├── editar_produto.html
    ├── index.html
    ├── login.html
    └── PaginaDaAdmin.html
```

---

## Instalação

```bash
git clone https://github.com/seuusuario/lojavirtual.git
```

```bash
cd lojavirtual
```

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

---

## Como Executar

```bash
python app.py
```

A aplicação roda localmente e expõe as rotas de login, catálogo e painel administrativo.

---

## Rotas da API

### `GET /`
Catálogo de produtos, visível para usuários comuns.

### `GET /login` e `POST /login`
Tela de autenticação. Define o tipo de usuário (`admin` ou `usuario`) e redireciona de acordo com a permissão.

### `GET /produtos`
Retorna a lista de produtos cadastrados, em formato JSON.

### `POST /produtos`
Adiciona um novo produto. Restrito a administradores.

**Request (multipart/form-data):**
```
nome: "Tênis Esportivo"
descricao: "Confortável e leve"
imagem: [arquivo]
```

**Response:**
```json
{
  "mensagem": "Produto adicionado com sucesso!"
}
```

### `POST /editar_produto/<index>`
Atualiza nome e descrição de um produto específico, identificado pelo índice. Restrito a administradores.

### `POST /excluir_produto/<index>`
Remove um produto específico do catálogo. Restrito a administradores.

---

## Sistema de Login

O acesso é feito através da tela `login.html`. Após a autenticação (usuário/senha fixos para testes), o sistema define o tipo de usuário:

- **admin** → redirecionado para `PaginaDaAdmin.html`
- **usuario** → redirecionado para `index.html`

> E-mails e senhas de teste estão documentados separadamente para fins de avaliação do projeto.

---

## Controle de Permissões

| Ação | Administrador | Usuário comum |
|---|---|---|
| Visualizar catálogo | ✅ | ✅ |
| Cadastrar produto | ✅ | ❌ |
| Editar produto | ✅ | ❌ |
| Excluir produto | ✅ | ❌ |

O controle é feito no backend, validando o tipo de usuário através da variável de sessão a cada requisição protegida.

---

## Banco de Dados

O projeto usa um arquivo JSON (`banco_produtos.json`) como banco de dados principal dos produtos, com a seguinte estrutura:

```json
[
  {
    "nome": "Tênis Esportivo",
    "descricao": "Confortável e leve",
    "imagem": "static/uploads/tenis.png"
  }
]
```

Cada novo produto é adicionado ao final do array. A edição altera os valores de acordo com o índice do item na lista.

---

## Fluxo do Sistema

```
Login
  ↓
Verificação de tipo de usuário
  ↓
admin → Painel Administrativo
usuario → Catálogo (somente visualização)
  ↓
Cadastro / Edição / Exclusão de produtos (admin)
  ↓
Atualização do banco_produtos.json
```

---

## Funcionalidades

- Sistema de login com diferenciação de permissões (admin / usuário)
- Catálogo de produtos com visualização pública
- Cadastro de produtos com upload de imagem
- Edição de nome e descrição de produtos existentes
- Exclusão de produtos
- Interface responsiva para mobile
- Animações de entrada por scroll (Intersection Observer)
- Favicon e identidade visual personalizados

---

## Roadmap

- [ ] Variáveis de ambiente via `.env` para senhas e chaves secretas
- [ ] Configuração separada para development e production
- [ ] Migração de SQLite/JSON para PostgreSQL ou MySQL em produção
- [ ] Refatoração visual com Bootstrap ou Tailwind CSS
- [ ] Sidebar responsiva para mobile
- [ ] Autenticação robusta com Flask-Login
- [ ] Proteção contra CSRF (Flask-WTF ou Flask-SeaSurf)
- [ ] Carrinho de compras e checkout
- [ ] Integração de pagamento (Stripe, Mercado Pago ou PayPal)
- [ ] Sistema de comentários e avaliações de produtos
- [ ] Envio de e-mails (confirmação de pedido, contato)
- [ ] Monitoramento de erros com Sentry
- [ ] Logs personalizados para acessos e erros críticos

---

## Segurança

- Controle de acesso por tipo de usuário validado no backend
- Identificação de pontos de melhoria em boas práticas (senhas, variáveis sensíveis) durante o desenvolvimento
- Primeiros passos com autenticação de administradores

> Este projeto está em estágio de aprendizado em relação a segurança — os itens de melhoria estão listados no Roadmap.

---

## Deploy

| Camada | Serviço |
|---|---|
| Aplicação completa | Render |

A escolha pelo Render se deu pela compatibilidade direta com aplicações Python/Flask e pelo plano gratuito disponível para projetos de portfólio.

**Configurações utilizadas:**
- `requirements.txt` com todas as dependências do projeto
- `Procfile` definindo o comando de inicialização com `gunicorn`
- Auto Deploy ativado, atualizando a aplicação automaticamente após cada `git push`
- Pasta `static/` configurada para arquivos públicos (CSS, imagens, uploads)

---

## Erros Reais Resolvidos

Durante o desenvolvimento e deploy, alguns problemas comuns de produção foram enfrentados e solucionados:

- **502 Bad Gateway** — erro típico de configuração incorreta de deploy, relacionado à porta e ao comando de inicialização
- **Conexão com banco de dados** — ajustes na manipulação de arquivos e caminhos entre ambiente local e produção
- **Aviso de senha comprometida** — identificado pelo navegador, corrigido com a adoção de boas práticas de senha

---

## Aprendizados

Este projeto foi um marco no aprendizado de desenvolvimento web full stack, com destaque para:

**Flask e backend**
- Criação de uma aplicação do zero com Python e Flask
- Estruturação de rotas e uso de templates com `render_template`
- Organização do projeto em `static/` e `templates/`

**Frontend**
- Estruturação e estilização de páginas com HTML, CSS e JavaScript
- Ajustes de responsividade para diferentes dispositivos
- Personalização de identidade visual (favicon, fontes, paleta)

**Banco de dados**
- Uso de JSON e SQLite para persistência local de dados
- Entendimento de como o Flask interage com o banco de forma síncrona

**Deploy em nuvem**
- Publicação da aplicação Flask no Render
- Configuração de `requirements.txt` e `Procfile`
- Uso de `gunicorn` como servidor de produção
- Entendimento do fluxo de Auto Deploy via `git push`

**Resolução de problemas reais**
- Diagnóstico e correção de erro 502 Bad Gateway
- Tratamento de problemas de conexão, porta e estrutura de arquivos
- Identificação de alertas de segurança do navegador e correção por boas práticas

---

## Conclusão

Este projeto foi uma excelente oportunidade para colocar em prática conhecimentos de desenvolvimento web full stack, com foco em Python e Flask. Ao longo do processo, foi possível construir uma loja virtual com painel administrativo completo — integrando HTML, CSS, JavaScript, persistência de dados e deploy real em nuvem. A experiência trouxe confiança para encarar projetos web mais robustos, com práticas mais próximas do que é utilizado em ambientes de produção.
