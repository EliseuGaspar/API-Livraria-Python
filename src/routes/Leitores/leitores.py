from flask import jsonify, request
from ...errors import error
from ...models.Leitor import Leitores
from ...authorize.permission import Permissions
from ...app import app


__leitores = Leitores()
__p = Permissions()

@app.route('/Leitores', methods=['GET'])
def Point_Leitores():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__leitores.leitores())
    else: return error(2)

@app.route('/AddLeitores', methods=['POST'])
def Point_AddLeitores():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__leitores.addleitores(dados["Leitores"]))
    else: return error(2)

@app.route('/DeleteLeitores', methods=['DELETE'])
def Point_DeleteLeitores():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__leitores.deleteleitores(dados["Leitores"]))
    else: return error(2)

@app.route('/UpdateLeitores', methods=['PUT'])
def Point_UpdateLeitores():
    dados = request.json
    if(__p.AuthorizeAcess(dados["acess"])):
        return jsonify(__leitores.updateleitores(dados["Leitores"],dados["Update"]))
    else: return error(2)