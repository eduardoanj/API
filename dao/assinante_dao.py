import MySQLdb
from model.assinante import Assinante


class AssinanteDao:
    def __init__(self):
        pass

    def list_all(self):
        connection = MySQLdb.connect(
                                    host="mysql.zuplae.com"  
                                    ,user="zuplae13" 
                                    ,passwd="grupo08"
                                    ,database="zuplae13"
                                )

        cursor = connection.cursor()
        cursor.execute("SELECT id, nome, cpf FROM assinante") 
        list_assinante = []   
        for p in cursor.fetchall():
            assinante = Assinante(p[1], p[2], p[0])
            list_assinante.append(assinante.__dict__)
        connection.close()
        return list_assinante

    def assinante_by_id(self, id):
        connection = MySQLdb.connect(
                                    host="mysql.zuplae.com"  
                                    ,user="zuplae13" 
                                    ,passwd="grupo08"
                                    ,database="zuplae13"
                                )

        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nome, cpf FROM assinante WHERE id = {id}")
        p = cursor.fetchone()
        assinante = Assinante(p[1], p[2], p[0])
        connection.close()
        return assinante.__dict__

    def create(self, assinante:Assinante):
        connection = MySQLdb.connect(
                                    host="mysql.zuplae.com"  
                                    ,user="zuplae13" 
                                    ,passwd="grupo08"
                                    ,database="zuplae13"
                                )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO assinante (nome, cpf) VALUES('{assinante.nome}','{assinante.cpf}')")
        assinante.id = cursor.lastrowid
        connection.commit()
        connection.close()
        return assinante.__dict__

    def update(self, assinante:Assinante):
        connection = MySQLdb.connect(
                                    host="mysql.zuplae.com"  
                                    ,user="zuplae13" 
                                    ,passwd="grupo08"
                                    ,database="zuplae13"
                                )
        cursor = connection.cursor()
        cursor.execute(f"UPDATE assinante SET nome ='{assinante.nome}', cpf = '{assinante.cpf}' WHERE id = {assinante.id}")
        connection.commit()
        connection.close()
        return assinante.__dict__

    def delete(self, id:int):
        connection = MySQLdb.connect(
                                    host="mysql.zuplae.com"  
                                    ,user="zuplae13" 
                                    ,passwd="grupo08"
                                    ,database="zuplae13"
                                )
        cursor = connection.cursor()
        cursor.execute(
                        f"DELETE FROM assinante WHERE id = {id}"
                    )
        connection.commit()
        connection.close()
