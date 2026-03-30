from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from  model import Base


class LivroModel(Base):
    __tablename__ = 'livro'

    id = Column("pk_livro", Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(100), nullable=False)
    editora = Column(String(100), nullable=False)
    isbn = Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=False)
    idioma = Column(String(50), nullable=False)
    lido = Column(String(1), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, titulo:str, autor:str, editora:str, isbn:str, ano:int, tipo:str, idioma:str, lido:str = 'N',
                 data_insercao:Union[DateTime, None] = None):
        """
        Cadastra um Livro

        Camopos:
            titulo: título do livro.
            autor: autor do livro.
            editora: editora do livro.
            isbn: ISBN do livro.
            ano: ano de publicação do livro.
            tipo: tipo do livro.
            idioma: idioma do livro.
            lido: status de leitura do livro.
            data_insercao: data de quando o livro foi inserido à base.
        """
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.isbn = isbn
        self.ano = ano
        self.tipo = tipo
        self.idioma = idioma
        self.lido = lido
        # se não for informada, será o data exata da inserção do livro à base
        if data_insercao:
            self.data_insercao = data_insercao
