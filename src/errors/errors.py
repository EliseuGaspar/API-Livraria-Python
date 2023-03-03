
def error(type : int) -> dict:
    if type == 1:
        return {
            "status":404,
            "Error.EndPoint":"EndPoint Errado."
        }
    if type == 2:
        return {
            "status":404,
            "Error.Acess":"Sem permissão de acesso."
        }