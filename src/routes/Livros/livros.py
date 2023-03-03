# -
# -
# -

from flask import jsonify, request
from ...errors import error
from ...models.Livro import Livros
from ...authorize.permission import Permissions
from ...app import app


__livros = Livros()
__p = Permissions()

@app.route('/Livros')
def Point_Livros():
    return jsonify(__livros.livros())

@app.route('/AddLivros', methods=['POST'])
def Point_Add_Livros():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__livros.addlivros(dados["Livros"]))
    else: return error(2)

@app.route('/DeleteLivros', methods=['DELETE'])
def Point_DeleteLivros():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__livros.deletelivros(dados["Livros"]))
    else: return error(2)

@app.route('/UpdateLivros', methods=['PUT'])
def Point_UpdateLivros():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__livros.updatelivros(dados["Livros"],dados["Update"]))
    else: return error(2)