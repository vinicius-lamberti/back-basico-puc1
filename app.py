from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

from schemas import LivroBuscaIdSchema, LivroViewSchema, ListagemLivrosSchema, LivroSchema, LivroDelSchema, LivroPatchSchema, ErrorSchema
from schemas.error import ErrorSchema404, ErrorSchema409
from schemas.livro import apresenta_livros

# Configuração da API
info = Info(title="API de Livros", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Configuração do SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Tag para o Swagger
book_tag = Tag(name="Livros", description="Gerenciamento do inventário de livros")

# --- Modelo do Banco de Dados conforme a Interface ---
class LivroModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(200), nullable=False)
    editora = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(17), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    idioma = db.Column(db.String(50), nullable=False)
    lido = db.Column(db.String(1), default='N') # 'S' ou 'N'

# --- Endpoints ---

@app.get('/', tags=[book_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')


@app.get('/livros', tags=[book_tag], responses={"200": ListagemLivrosSchema})
def get_livros():
    """Busca os livros cadastrados"""
    livros = LivroModel.query.all()
    return apresenta_livros(livros), 200

@app.post('/livro', tags=[book_tag], responses={"201": LivroViewSchema, "400": ErrorSchema, "409": ErrorSchema409})
def post_book(form: LivroSchema):
    """Cadastra um livro"""

    campos_obrigatorios = ['titulo', 'autor', 'editora', 'isbn', 'ano', 'tipo', 'idioma']
    
    for campo in campos_obrigatorios:
        # getattr pega o valor do campo dentro do objeto 'form'
        if getattr(form, campo) is None or getattr(form, campo) == "":
            return {"message": f"Campo '{campo}' é obrigatório"}, 400
        
    
        
    livro = LivroModel.query.filter_by(isbn=form.isbn).first()
    if livro:
        return {"message": "Já existe um livro com esse ISBN."}, 409

    novo_livro = LivroModel(
        titulo=form.titulo,
        autor=form.autor,
        editora=form.editora,
        isbn=form.isbn,
        ano=form.ano,
        tipo=form.tipo,
        idioma=form.idioma,
        lido=form.lido or 'N'
    )
    
    db.session.add(novo_livro)
    db.session.commit()
    
    return {
        "id": novo_livro.id, "titulo": novo_livro.titulo, "autor": novo_livro.autor,
        "editora": novo_livro.editora, "isbn": novo_livro.isbn, "ano": novo_livro.ano,
        "tipo": novo_livro.tipo, "idioma": novo_livro.idioma, "lido": novo_livro.lido
    }, 201

@app.delete('/livro', tags=[book_tag], responses={"200": LivroDelSchema, "404": ErrorSchema404})
def delete_book(query: LivroBuscaIdSchema):
    """Deleta um livro via id"""
    livro = LivroModel.query.get(query.id)
    if not livro:
        return {"message": "Livro não encontrado"}, 404
    
    livro_titulo = livro.titulo
    
    db.session.delete(livro)
    db.session.commit()
    return {"message": f"Livro '{livro_titulo}' removido com sucesso"}, 200

@app.patch('/livro', tags=[book_tag], responses={"200": LivroViewSchema, "404": ErrorSchema404, "400": ErrorSchema})
def patch_book(query: LivroBuscaIdSchema, form: LivroPatchSchema):
    """Atualiza o status de leitura do livro via id"""
    if not form.lido:
        return {"message": "Campo 'lido' é obrigatório"}, 400

    livro = LivroModel.query.get(query.id)
    if not livro:
        return {"message": "Livro não encontrado"}, 404

    livro.lido = form.lido
    db.session.commit()

    return {
        "id": livro.id, "titulo": livro.titulo, "autor": livro.autor,
        "editora": livro.editora, "isbn": livro.isbn, "ano": livro.ano,
        "tipo": livro.tipo, "idioma": livro.idioma, "lido": livro.lido
    }, 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)