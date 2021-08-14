#!/usr/bin/env python

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from conexion.conexion import Conexion
import hashlib

class daoUser:
    
    def createTableUser(self):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USERS'")
            #print(self.__mi_cursor.fetchone()[0])

            if cursor.fetchone()[0] == 1:
                return "This table exists!"
            else:
                cursor.execute('''
                    CREATE TABLE USERS(
                    ID INTEGER PRIMARY KEY,
                    USERNAME VARCHAR(50) UNIQUE,
                    PASSWORD VARCHAR(128) UNIQUE)
                        ''')
                return "Table created successfully"
            con.commit()
            cursor.close()
            con.close()
        
        except Exception as e:
            print("Error to create table users: ", e)

    def createUser(self, name="", passwd=""):
        try:
            passwd = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute('SELECT MAX(ID) FROM USERS')
            ide = cursor.fetchall()[0][0]
            #ide = 0
            print(ide)
            if ide == None:
                ide = 1
            else:
                ide += 1

            print(ide)

            usuario = (ide, name, passwd)
            orderSQL = "INSERT INTO USERS (ID, USERNAME, PASSWORD) VALUES(?,?,?)"
            cursor.execute(orderSQL, usuario)
            con.commit()
            cursor.close()
            con.close()

        except Exception as e:
            print("Error to create users ", e)

    def updateUser(self, name="", passwd=""):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            passwd = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
            orderSQL = "UPDATE USERS SET password=? WHERE USERNAME=?"
            datosPersonales = (passwd, name)
            cursor.execute(orderSQL, datosPersonales)
            con.commit()
            cursor.close()
            con.close()
        except Exception as e:
            print(e)
        
    def deleteUser(self, name=""):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            orderSQL = "DELETE FROM USERS WHERE USERNAME=?"
            name = (name, )
            cursor.execute(orderSQL, name)
            con.commit()
            cursor.close()
            con.close()
            
        except Exception as e:
            print(e)

    def selectUser(self, username=""):
        datos = None
        con = None
        cursor = None
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            orderSql = "SELECT ID, USERNAME, PASSWORD FROM USERS WHERE USERNAME=?"
            username = (username, )
            cursor.execute(orderSql, username)
            usuarios = cursor.fetchall()
            cursor.close()
            con.close()
            for usuario in usuarios:
                datos = (usuario)
        except Exception as e:
            print(e)
        return datos



