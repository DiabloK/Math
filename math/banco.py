import sqlite3

class Banco(object):
    def __init__(self):
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = sqlite3.connect('escola.db')
            self.his="CREATE TABLE IF NOT EXISTS histo " \
                      "(hipotenusa INTEGER NOT NULL ,catetoAd INTEGER not null,catetoO interger not null);"
            self.conexao.execute(self.his)
            self.conexao.commit()
        except sqlite3.Error as erro:
            print(erro.args[0])

    def desconectar(self):
        self.conexao.close()