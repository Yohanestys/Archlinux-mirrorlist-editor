#!/usr/bin/env python3

from sys import argv

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from file.file import generated_mirrorlist

if __name__ == "__main__":
    a = ""
    if len(argv) == 2:
        a = argv[1]

    class Mirrorlist:
        __new_file = ""
        __country = ""
        __mirrorlist_pacnew = ""

        def __init__(self, c=""):
            self.__new_file = "This country not exists!"
            self.__country = c
            self.__mirrorlist_pacnew = "/etc/pacman.d/mirrorlist.pacnew"
            try:
                if not os.path.isfile(self.__mirrorlist_pacnew):
                    ruta = self.__mirrorlist_pacnew[0:self.__mirrorlist_pacnew.rfind("/")+1]
                    if not os.path.exists(ruta):
                        os.makedirs(ruta)
                    with open(self.__mirrorlist_pacnew, "w") as file:
                        file.write(generated_mirrorlist())
                        file.close()

                if self.__country != "":
                    self.__mirror_list_country()
                    print(len(c))
                else:
                    self.__entire_mirror_list()
                    print(len(c))
            except Exception as e:
                print("Some error happened ", e)
                
        def __mirror_list_country(self):
            try:
                with open(self.__mirrorlist_pacnew, "r") as file:
                    for fichero in file:
                        if fichero.startswith("## " + self.__country):
                            self.__new_file = fichero
                            for f in file: 
                                if not f.startswith("## "):
                                    self.__new_file += f[1:]
                                if "## " in f:
                                    break
                    file.close()
            except FileNotFoundError as noExists:
                self.__new_file = "File not exists" + str(noExists)

            return self.__new_file

        def __entire_mirror_list(self):
            try:
                with open(self.__mirrorlist_pacnew, "r") as file:
                    self.__new_file = ""
                    for f in file:
                        if f.startswith("#Server"):
                            # f = f.replace(f, f[1:])
                            # self.__new_file += f
                            self.__new_file += f[1:]
                        else:
                            self.__new_file += f
                    file.close()
            except FileNotFoundError as noExists:
                self.__new_file = "File not exists " + str(noExists)
            return self.__new_file

        def create_new_mirror_list(self):
            try:
                if self.__new_file != "This country not exists!":
                    if self.__new_file.startswith("File not exists"):
                        with open("/etc/pacman.d/mirrorlist", "a") as file:
                            file.write("\n###\n# "+self.__new_file+"\n###")
                            file.close()
                    else:
                        with open("/etc/pacman.d/mirrorlist", "w") as file:
                            file.write(self.__new_file)
                            file.close()
            except PermissionError:
                print("You do not have permitions to make changes in the mirrorlist")

        def getNewFile(self):
            return self.__new_file

        def resultadoFichero(self):                                                     
            res = ""
            try:
                with open("/etc/pacman.d/mirrorlist", "r") as file:
                    res = file.read()
                    file.close()
                    
            except FileNotFoundError as notFound:
                res = "The file not exist!" 
            return res


    create_mirrorlist = Mirrorlist(a)
    create_mirrorlist.create_new_mirror_list()
    #print(create_mirrorlist.resultadoFichero())

else:

    def resultadoFichero():                                                         
        res = ""
        try:
            with open("/etc/pacman.d/mirrorlist", "r") as file:                         
                res = file.read()                                                              
            file.close()
        except FileNotFoundError as notFound:
            res = "The file not exist!"
        return res      
    #res = resultadoFichero()
    #print(res)

    def countries():
        country = []
        mirrorlist_pacnew = "/etc/pacman.d/mirrorlist.pacnew"    
        try:
            if not os.path.isfile(mirrorlist_pacnew):
                with open("/tmp/generated_mirrorlist.pacnew", "w") as file:
                    file.write(generated_mirrorlist())
                    file.close()
                with open("/tmp/generated_mirrorlist.pacnew", "r") as file:
                    for f in file:
                        if f.startswith("## "):
                            if file.readline().startswith("#Server"):
                                country.append(f[3:-1])
                    file.close()
            else:
                with open(mirrorlist_pacnew, "r") as file:
                    for f in file:
                        if f.startswith("## "):
                            if file.readline().startswith("#Server"):
                                country.append(f[3:-1])
                    file.close()
        
        except FileNotFoundError as noExists:
            country.append("File not exists "+ str(noExists))
        
        except Exception as e:
            country.append("File not exists "+ str(noExists))   
        
        return country

#exit(0)

