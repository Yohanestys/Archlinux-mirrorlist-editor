#!/usr/bin/env python

import sqlite3
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path = os.path.dirname(currentdir)

#path = os.path.abspath('../')

class Conexion:
    __mi_conexion = None

    def __init__(self, db=path+"/bd/users.db"):
        try:
            if not os.path.exists(db[:db.rfind("/")]):                          
                os.makedirs(db[:db.rfind("/")])  
            self.__mi_conexion = sqlite3.connect(db)
        except Exception as e:
            print("Some error: ", e)
    def setConexion(self, bd=path+"/bd/users.db"):
        try:
            if not os.path.exists(db[:db.rfind("/")]):
                os.makedirs(db[:db.rfind("/")])
            self.__mi_conexion = sqlite3.connect(db)                     
        except Exception as e:
            print("Some error: ", e)
    def getConexion(self):
        return self.__mi_conexion


if __name__ == '__main__':
    conexion = Conexion()
    print(conexion.getConexion())
    
