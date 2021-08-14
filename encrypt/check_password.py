#!/usr/bin/env python

import subprocess
from subprocess import PIPE
from getpass import getpass
from getpass import getuser
from subprocess import check_output
try:
    from crypt import crypt
except ImportError as im:
    print("Import error", im)


def check_password(passwd):
    correcto = False
    try:        
        usuario = getuser()
        command_line = "echo {} | sudo -S grep -w {} /etc/shadow | cut -d: -f2".format(passwd, usuario)
        shell_command = check_output(command_line, shell=True)
        
        # la contraseña enctiptada deontro del fichero /etc/shadow
        original_hash_passwd = shell_command.decode("utf-8").strip("\n")

        # el index donde se encuentra el segundo $ +1
        start_salt_value = original_hash_passwd[1:].find("$")+1 #mas uno es para no incluir el $ dentro del valor generado

        # el index donde se encuentra el segundo dolar o lo que es el final de salt value sin incluir el $
        end_salt_value = original_hash_passwd.rfind("$")

        # salt value
        salt_value = original_hash_passwd[start_salt_value:end_salt_value] #ponemos el index a si no queremos incliur el primer $

        # inicio del código hash
        start_hash = original_hash_passwd.find("$")

        # fin del código hash
        end_hash = start_hash+2

        # código hash
        hash_algoritm = original_hash_passwd[start_hash:end_hash]

        # generar el password usando el algoritmo hash + salt_value
        generated_passwd = crypt(passwd, hash_algoritm+salt_value)
    
        if original_hash_passwd == generated_passwd:
            correcto = True
        
    except Exception as e:
        print("Some error occurred ",e)
        
    return correcto

if __name__ == '__main__':
    passwd = getpass(prompt="\nWrite your passwd please: ", stream=None)
    check_password(passwd)


