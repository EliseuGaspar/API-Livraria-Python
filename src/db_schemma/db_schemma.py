import json as j


class DB():
    def __init__(self) -> None:
        self.__bd__ = j
    
    def GET(self) -> dict:
        """Faz uma leitura do arquivo json e retorna todo o conteudo em um tipo 'Dict' [Dicionário]."""
        with open('src/database/data.json','r',encoding='utf-8') as db:
            content = db.read()    
        return self.__bd__.loads(content)

    def Insert(self, data : dict, acess : str) -> bool:
        conteudo = self.GET()
        
        if acess == 'Livros':
            DICT = {
                "Leitores":conteudo["Leitores"],
                "Livros":data
            }
        else:
            DICT = {
                "Leitores":data,
                "Livros":conteudo["Livros"]
            }
        with open('src/database/data.json','w',encoding='utf-8') as db:
            self.__bd__.dump(DICT,db,indent=4,sort_keys=True)
        
        if self.GET() == None or self.GET() == '' or self.GET() == '{}':
            return False    
        return True