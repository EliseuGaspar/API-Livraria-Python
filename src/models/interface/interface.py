import random as r
from ...db_schemma import DB

class model:
    db = DB()
    
    def __init__(self) -> None:
        self.db = DB()
    
    def __metadados__(self, obj : dict, id_class : str) -> dict:
        if id_class == 'Livros':
            return {
                "Nome" : obj['Nome'],
                "quant." : obj['quant.'],
                "prat." : obj["quant."],
                "disp.":True,
                "id":f"{r.randint(10,90)}{r.randint(10,90)}"
            }
        else:
            return {
                "Nome": obj['Nome'],
                "e-mail": obj['e-mail'],
                "id": f"{r.randint(10,80)}{r.randint(10,70)}",
                "livros": [],
                "phone_number": obj['phone_number']
            }
    
    def __searching__(self, obj : list, id_class : str = '', key : str = 'id') -> int:
        if id_class == 'Livros':
            list_obj = self.db.GET()[id_class]
            print(f"datas : {self.db.GET()[id_class]}")
            index = None
            count = 0
            for livro in list_obj:
                if livro[key] == obj:
                    index = count
                count += 1
            return index
        else:
            list_obj = self.db.GET()[id_class]
            print(f"datas : {self.db.GET()[id_class]}")
            index = None
            count = 0
            for livro in list_obj:
                if livro[key] == obj:
                    index = count
                count += 1
            return index
      
    def __change__(self, obj : dict, obj_after : dict, id_class : str) -> dict:
        if id_class == 'Livros':
            try: obj['Nome'] = obj_after['Nome']
            except: obj['Nome'] = obj['Nome']

            try: obj['disp.'] = obj_after['disp.']
            except: obj['disp.'] = obj['disp.']

            try: obj['quant.'] = obj_after['quant.']
            except: obj['quant.'] = obj['quant.']

            try: obj['prat.'] = obj_after['prat.']
            except: obj['prat.'] = obj['prat.']
        else:
            try: obj['Nome'] = obj_after['Nome']
            except: obj['Nome'] = obj['Nome']

            try: obj['e-mail'] = obj_after['e-mail']
            except: obj['e-mail'] = obj['e-mail']

            try: obj['phone_number'] = obj_after['phone_number']
            except: obj['phone_number'] = obj['phone_number']

            try: obj['Livros'] = []
            except: obj['Livros'] = []
        return obj

    def __permission__(self, obj : dict, id_class : str, key : str = 'full'):
        if id_class == 'Livros':
            if key == 'full':
                if self.__searching__(obj['Nome'],id_class,'Nome') != None:
                    print('entrou !')
                    return True
                else:
                    print('Não Entrou!')
                    return False
            else:
                if self.__searching__(obj[key],id_class,key) != None: return True
                else: return False
        else:
            if key == 'full':
                if self.__searching__(obj['Nome'],id_class,'Nome') != None or self.__searching__(obj['phone_number'],id_class,'phone_number') != None or self.__searching__(obj['e-mail'],id_class,'e-mail') != None:
                    return True
                else:
                    return False
            else:
                if self.__searching__(obj[key],id_class,key) != None: return True
                else: return False

    def adicionar(self, obj : dict, id_class : str) -> dict:

        new_obj = self.db.GET()[id_class]
        alert = False
        data_alert = []

        for obj_ in obj:
            if(self.__permission__(obj_,id_class)):
                alert = True
                data_alert.append(obj_['Nome'])
            else:
                obj_ = self.__metadados__(obj_, id_class)
                new_obj.append(obj_)
        
        if not alert:
            self.db.Insert(new_obj, id_class)
        else:
            return {
                "response":f"Não foi possível adicionar estes {id_class.lower()} porque há dados semelhantes de {id_class.lower()} existentes na base de dados. {id_class}: {data_alert}"
            }

        return self.db.GET()[id_class]

    def remover(self, obj : tuple = (), id_class : str = '') -> list | dict:
        list_objs_ = self.db.GET()[id_class]
        values = 0
        for obj_ in obj:
            index = self.__searching__(obj_, id_class)
            if index != None:
                list_objs_.pop(index)
                self.db.Insert(list_objs_, id_class)
                values += 1
                print(values)
        if values != 0:
            return list_objs_
        
        return {'response':f'Não foram encontrados {id_class} com tais id na base de dados!'}

    def atualizar(self, old_obj : tuple(), new_obj : tuple(), id_class : str) -> dict:
        list_objs_ = self.db.GET()[id_class]
        ii = 0
        for obj_ in old_obj:
            index = self.__searching__(obj_, id_class)
            if index != None:
                list_objs_.append(self.__change__(list_objs_[index],new_obj[ii]),id_class)
                list_objs_.pop(index)
            ii += 1
        self.db.Insert(list_objs_, id_class)

        return self.db.GET()[id_class]



