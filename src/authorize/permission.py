import json


def __Reading__() -> dict:

    with open('src/database/admin/data.json',encoding='utf-8') as k:
        conteudo = k.read()
        conteudo_json = json.loads(conteudo)
    
    return conteudo_json


class Permissions():

    def AuthorizeAcess(self, datas) -> bool:
        keys = __Reading__()
        if keys['id'] == datas['id'] and keys['password'] == datas['password']:
            return True
        else: return False