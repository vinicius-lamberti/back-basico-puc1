from pydantic import BaseModel, Field, field_validator
from typing import List
from model.livro import LivroModel

class LivroSchema(BaseModel):
    titulo: str
    autor: str
    editora: str
    isbn: str
    ano: int
    tipo: str
    idioma: str
    lido: str

    @field_validator('isbn', mode='before')
    @classmethod
    def validate_isbn(cls, v):
        if isinstance(v, int):
            return str(v)
        return v


class LivroPatchSchema(BaseModel):
    lido: str = Field(..., example='S')


class LivroBuscaSchema(BaseModel):
    id: int


from pydantic import Field

class LivroViewSchema(BaseModel):
    id: int = Field(..., example=1)
    titulo: str = Field(..., example="O Hobbit")
    autor: str = Field(..., example="J. R. R. Tolkien")
    editora: str = Field(..., example="Harper Collins")
    isbn: str = Field(..., example="9788595084742")
    ano: int = Field(..., example=2019)
    tipo: str = Field(..., example="Livro")
    idioma: str = Field(..., example="Português")
    lido: str = Field(..., example="S")


class ListagemLivrosSchema(BaseModel):
    livros: List[LivroViewSchema] = Field(..., example=[
        {
            "id": 1,
            "titulo": "O Hobbit",
            "autor": "J. R. R. Tolkien",
            "editora": "Harper Collins",
            "isbn": "9788595084742",
            "ano": 2019,
            "tipo": "Livro",
            "idioma": "Português",
            "lido": "S"
        }
    ])


class LivroDelSchema(BaseModel):
    message: str
    id: int


def apresenta_livro(livro: LivroModel):
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "editora": livro.editora,
        "isbn": livro.isbn,
        "ano": livro.ano,
        "tipo": livro.tipo,
        "idioma": livro.idioma,
        "lido": livro.lido
    }


def apresenta_livros(livros: List[LivroModel]):
    return {"livros": [apresenta_livro(livro) for livro in livros]}