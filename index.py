#!/usr/bin/env python3
import os
import subprocess
from subprocess import PIPE
from getpass import getpass
from mirrorlist import countries                                             

try:
    
    country = input("Write the new country for the mirrorlist servers: ")           
    passwd = getpass(prompt="Write your user password: ", stream=None)              
    echo = subprocess.Popen(['echo', passwd], stdout=PIPE)    
    createFile = subprocess.Popen(['sudo', '-S', './mirrorlist.py', country], stdin=echo.stdout, stdout=PIPE, stderr=PIPE)
    output1 = createFile.stdout.read().decode()
    output2 = createFile.stderr.read().decode()
    print("Correcto ", output1)
    print("Error ", output2)
    
    
    for i, country in enumerate(countries()):
        print("Country", (i+1), country)

    #out, err = createFile.communicate(input=(passwd+'\n').encode(), timeout=5)
    #except subprocess.TimeoutExpired:
    #    createFile.kill()
except KeyboardInterrupt:
    print("\n¡Bye!")
    exit(0)

#print(countries())                                                       


