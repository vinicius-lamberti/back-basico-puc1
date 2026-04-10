from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    message: str

class ErrorSchema404(ErrorSchema):
    """ Define como uma mensagem de erro 404 será representada
    """
    message: str = "Livro não encontrado"

class ErrorSchema409(ErrorSchema):
    """ Define como uma mensagem de erro 409 será representada
    """
    message: str = "Já existe um livro com esse ISBN."