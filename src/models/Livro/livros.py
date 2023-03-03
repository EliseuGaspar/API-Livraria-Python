from ..interface import model

class Livros(model):
    def __init__(self) -> None:
        super().__init__()
    
    def livros(self, ) -> dict: return super().db.GET()['Livros'] # Retorna uma lista com todos os livros registrados
    
    def addlivros(self, obj : dict) -> dict: # Adiciona ' n ' livros a base de dados
        return super().adicionar(obj,'Livros')

    def deletelivros(self, livros : tuple = ()) -> dict: # Remove ' n ' livros da base de dados
        return super().remover(livros,'Livros')

    def updatelivros(self, livros : tuple = (), updates : tuple = ()) -> list | dict: # Atualiza ' n ' livros da base de dados
        return super().atualizar(livros,updates,'Livros')


