from ..interface.interface import model


class Leitores(model):
    def __init__(self) -> None:
        super().__init__()
    
    def leitores(self, ) -> dict: return super().db.GET()['Leitores']
    
    def addleitores(self, obj : dict) -> dict:
        return super().adicionar(obj,'Leitores')

    def deleteleitores(self, leitores : tuple = ()) -> dict:
        return super().remover(leitores,'Leitores')

    def updateleitores(self, leitores : tuple = (), updates : tuple = ()) -> list | dict:
        return super().atualizar(leitores,updates,'Leitores')

