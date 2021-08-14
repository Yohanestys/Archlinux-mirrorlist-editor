#!/usr/bin/env python3
import os
import subprocess
from subprocess import PIPE
from getpass import getpass
from getpass import getuser

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

try:
    from ttkthemes import ThemedStyle
except Exception as e:
    print(e)

# import method from tha package mirrorlist
from mirrorlist import resultadoFichero                             
from mirrorlist import countries
from dao.daoUser import daoUser
from encrypt.check_password import check_password 
import hashlib

# Import la ventana del menu
from menuwindows.window import Window

def themes(r):
    global themeColor
    themeColor = StringVar()
    set_theme = StringVar()
    set_theme.set('arc')
    global style                                                                
    try:                                                                        
        if set_theme.get() == 'clam':                                           
            themeColor.set('#DCDAD5')                                           
            #Create a style                                                     
            style = ttk.Style(r)                                                
            # Set the theme with the theme_use method
            style.theme_use(set_theme.get()) #put the theme name here, that you want to use
        elif set_theme.get() == 'arc':                                          
            style = ThemedStyle(r)                                              
            themeColor.set('#F5F6F7')
            # Set the theme with the theme_use method
            style.theme_use(set_theme.get()) #put the theme name here, that you want to use
    except NameError:                                                           
        set_theme.set('clam')                                                   
        themeColor.set('#DCDAD5')                                               
        #Create a style                                                         
        style = ttk.Style(r)                                                    
        # Set the theme with the theme_use method 
        style.theme_use(set_theme.get()) #put the theme name here, that you want to use

    except ModuleNotFoundError:
        set_theme.set('clam')                                                   
        themeColor.set('#DCDAD5')                                               
        #Create a style                                                         
        style = ttk.Style(r)                                                    
        # Set the theme with the theme_use method 
        style.theme_use(set_theme.get()) #put the theme name here, that you want to use


def close(r, e=None):
    valor = messagebox.askokcancel("Close", "Do you want to close the aplication?")
    print(valor)
    if valor:
        print("\n¡Bye!")
        r.destroy()
    
    if e != None:
        e(0)

def about():
    #mensaje = messagebox.showinfo("Version", "About: 1.0v")
    about = Window()
    about.title("About mirrorlist app")
    themes(about)
    barMenu = Menu(about, bg=themeColor.get())
    about.config(menu=barMenu, width=710, height=300)
    def info():
        frame = Frame                                                           
        about.switch_frame(frame)                                               
        frame = about.frame                                                     
        frame.config(width=710, padx=22.5, pady=10, bg=themeColor.get())          
        label = ttk.Label(frame, text="Mirrorlist creator v1.0")                            
        label.grid(column=1, row=1, columnspan=3, padx=10, pady=10)         
        contenidoTexto = Text(frame, state=NORMAL, height=15)                   
        contenidoTexto.grid(column=1, columnspan=2, row=2, sticky="e", padx=10, pady=10)
        #contenidoTexto.delete("1.0", "end")                                    
        contenidoTexto.insert(INSERT, '''\n This application is oriented to be used on Archlinux or based on it distros.
        \n The application is written in python using tkinter like Desktop GUI.
         \n This application is a mirror list server selector that allows us to switch 
         between servers from some country that we like for better performance. 
         If we are traveling far from our country this is very useful.  
                                                                               
                ''')                                                            
        contenidoTexto.get("1.0", "end")                                        
        contenidoTexto.configure(state=DISABLED)
    
    info()
    def author_func():
        frame = Frame                                                           
        about.switch_frame(frame)                                               
        frame = about.frame                                                     
        frame.config(width=710, padx=22.5, pady=10, bg=themeColor.get())          
        label = ttk.Label(frame, text="Mirrorlist creator v1.0")                            
        label.grid(column=1, row=1, columnspan=3, padx=10, pady=10)         
        contenidoTexto = Text(frame, state=NORMAL, height=15)                   
        contenidoTexto.grid(column=1, columnspan=2, row=2, sticky="e", padx=10, pady=10)
        #contenidoTexto.delete("1.0", "end")                                    
        contenidoTexto.insert(INSERT, '''\n Autor: Yohanesty
        \n Nationality: Bulgaria
        \n Email: wallenty@gmail.com
                                                                                
                ''')                                                            
        contenidoTexto.get("1.0", "end")                                        
        contenidoTexto.configure(state=DISABLED) 

    def my_licence_func():
        frame = Frame
        about.switch_frame(frame)
        frame = about.frame
        frame.config(width=600, padx=10.49, pady=10, bg=themeColor.get())
        label = ttk.Label(frame, text="Mirrorlist creator v1.0")
        label.grid(column=1, row=1, columnspan=3, padx=10, pady=10)
        contenidoTexto = Text(frame, state=NORMAL, height=15)
        contenidoTexto.grid(column=1, columnspan=2, row=2, sticky="e", padx=10, pady=10)
        #contenidoTexto.delete("1.0", "end")
        scrollVert = ttk.Scrollbar(frame, command=contenidoTexto.yview) #Lo añadimos al contenidoTexto y le decimos que sea vertical
        #pero con esto no es suficiente, por esto tenemos que colocarlo con grid
        #vamos a cambiar el tamaño del scroll
        scrollVert.grid(column=3, row=2, sticky="nsew", padx=5, pady=5)
        # agregar posicionamiento del scroll según donde nos encontramos en la área del texto
        contenidoTexto.config(yscrollcommand=scrollVert.set)      
        contenidoTexto.insert(INSERT, '''\n MIT License
                \n\n Copyright (c) 2021 Yohanesty

                \n Permission is hereby granted, free of charge, to any person obtaining a copy
                \n of this software and associated documentation files (the "Software"), to deal
                \n in the Software without restriction, including without limitation the rights
                \n to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
                \n copies of the Software, and to permit persons to whom the Software is
                \n furnished to do so, subject to the following conditions:

                \n\n The above copyright notice and this permission notice shall be included in all
                \n copies or substantial portions of the Software.

                \n\n THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
                \n IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
                \n FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
                \n AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
                \n LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
                \n OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
                \n SOFTWARE.
                ''')
        contenidoTexto.get("1.0", "end")
        contenidoTexto.configure(state=DISABLED)

    #Licencia
    barMenu.add_command(label="About", command=info)
    barMenu.add_command(label="Autor", command=author_func)
    barMenu.add_command(label="Licence", command=my_licence_func)
    
    about.mainloop()

usuario = getuser()
root = None

nuevoPutoUsuario = daoUser()
nuevoPutoUsuario.createTableUser()

def createUser(password1, password2, r, label):
    if password1 == password2 and password1 != "" and password2 != "":
        if os.name == "nt":
            if nuevoPutoUsuario.selectUser(usuario) == None:                    
                nuevoPutoUsuario.createUser(usuario, password1)                 
                r.destroy()                                                    
            else:                                                               
                nuevoPutoUsuario.updateUser(usuario, password1)                 
                r.destroy()  
        else:
            if check_password(password1):
                if nuevoPutoUsuario.selectUser(usuario) == None:
                    nuevoPutoUsuario.createUser(usuario, password1)
                    #r.destroy()
                else:
                    nuevoPutoUsuario.updateUser(usuario, password1)
                    #r.destroy()
                label.config(text="Password correct", foreground="gray")
                textLabel = label.cget("text")
                if textLabel == "Password correct":
                    messagebox.showinfo(usuario.capitalize(), "Password correct!")
                    r.destroy()
            else:
                label.config(text="Incorrect password", foreground="red")
    else:
        label.config(text="Incorrect password", foreground="red")

    passwd1.set("")
    passwd2.set("")

def deleteUser(usuario, r):
    mensaje = messagebox.askquestion("Delete", "Are you sure to delete the user?")
    if mensaje == "yes":
        nuevoPutoUsuario.deleteUser(usuario)
        messagebox.showwarning("Delete", "User deleted")
        r.destroy()
    print(usuario)

def window_create_user(update=False):
    if root != None:
        root.destroy()
    datos = nuevoPutoUsuario.selectUser(usuario)
    global passwd1
    global passwd2
    while datos == None or update:
        root2 = Tk()
        root2.title("Validating password")
        passwd1 = StringVar()
        passwd2 = StringVar()
        formulario = Frame(root2)
        themes(root2)
        formulario.config(padx=10, pady=10, bg=themeColor.get())
        formulario.pack()
        labelUser = ttk.Label(formulario, text=usuario.capitalize()+" put your system password please")
        labelUser.grid(column=1, columnspan=2, row=1, padx=10, pady=10)
        
        myLab1 = ttk.Label(formulario, text="password:")
        myLab1.grid(column=1, columnspan=2, row=2, padx=10, pady=0)
        
        passwd1_entry = ttk.Entry(formulario, textvariable=passwd1)
        passwd1_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=5)
        passwd1_entry.config(show="*")
        
        myLab2 = ttk.Label(formulario, text="repeat password:")
        myLab2.grid(column=1, columnspan=2, row=4, padx=10, pady=0)   
        
        passwd2_entry = ttk.Entry(formulario, textvariable=passwd2)
        passwd2_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=5)
        passwd2_entry.config(show="*")

        checkButton = ttk.Button(formulario, text="Confirm", command=lambda:createUser(passwd1.get(), passwd2.get(), root2, labelUser))
        checkButton.grid(column=1, row=6, padx=10, pady=10)

        closeButton = ttk.Button(formulario, text="Close", command=lambda:close(root2, exit))
        closeButton.grid(column=2, row=6, padx=10, pady=10)
        root2.mainloop()

        #if datos == None:
        datos = nuevoPutoUsuario.selectUser(usuario)
        if update:
            window_mirror_list()
            update = False
        
    #print(datos[datos.index(usuario)])
    print(datos)

# ejecutamos el window_create_user la primera vez al iniciar la aplicación si no esta creado ningún usuario
window_create_user()

def createFile(country, passwd, m):
    if country.lower() == "all":
        country = ""
    print(country)
    passwdEncript = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
    print("Encipted ", passwdEncript)
    passwdBase = nuevoPutoUsuario.selectUser(usuario)[2]
    print("Pass base ", passwdBase)
    if passwdEncript == passwdBase:
        try:
            if os.name == "nt":
                labelText = ttk.Label(m, text="Error: ", foreground="red")
                resultado = ("\n To "+usuario.capitalize()+":"+"\n You are running Windows system and this application work correcly in"
                +"\n Archlinux-based distros!")
            else:
                echo = subprocess.Popen(['echo', passwd], stdout=PIPE)                  
                createFile = subprocess.Popen(['sudo', '-S', './mirrorlist.py', country], stdin=echo.stdout, stdout=PIPE, stderr=PIPE)
                output = createFile.stdout.read().decode("utf-8").strip("\n")                             
                outer = createFile.stderr.read().decode("utf-8").strip("\n")
                print("Correcto ", output)
                print("Error ", outer)                                                                
                resultado = resultadoFichero()                                  
                print(resultado)
            
            if resultado:
                labelText = None
                if resultado == resultadoFichero():
                    labelText = ttk.Label(m, text="Mirror list servers content: ")
                else:
                    labelText = ttk.Label(m, text="Error: ", foreground="red")
                labelText.grid(column=1, sticky="w", row=6, padx=10)
                contenidoTexto = Text(m, state=NORMAL, height=15)
                contenidoTexto.grid(column=1, columnspan=3, row=7, sticky="e", padx=10, pady=10)
                #contenidoTexto.delete("1.0", "end")
                scrollVert = ttk.Scrollbar(m, command=contenidoTexto.yview) #Lo añadimos al contenidoTexto y le decimos que sea vertical
                #pero con esto no es suficiente, por esto tenemos que colocarlo con grid
                #vamos a cambiar el tamaño del scroll
                scrollVert.grid(column=4, row=7, sticky="nsew", padx=5, pady=5)
                # agregar posicionamiento del scroll según donde nos encontramos en la área del texto
                contenidoTexto.config(yscrollcommand=scrollVert.set)
                
                contenidoTexto.insert(INSERT, resultado)
                contenidoTexto.get("1.0", "end")
                contenidoTexto.configure(state=DISABLED)
                                                                                
            #out, err = createFile.communicate(input=(passwd+'\n').encode(), timeout=5)
        
        except KeyboardInterrupt:
            print("\n¡Bye!")                                                        
            exit(0) 
    
    else:                                                                       
        labelText = ttk.Label(m, text="Error: ", foreground="red")                                
        labelText.grid(column=1, sticky="w", row=6, padx=10)                    
        resultado = ("\n To "+usuario.capitalize()+":"+"\n The system password and the app password must be the same!"
        +"\n Please verify your password! If you are considering that you are entering"
        +"\n the password correctly, then you must change it from 'User' application menu,"
        +"\n since you may have the password wrongly saved in the application.")
        if passwd == "":
            resultado = "\n To "+usuario.capitalize()+":"+"\n You can't leave the pasword blank!"
        contenidoTexto = Text(m, state=NORMAL, height=15)                       
        contenidoTexto.grid(column=1, columnspan=3, row=7, sticky="e", padx=10, pady=10)
        #contenidoTexto.delete("1.0", "end")                                    
        scrollVert = ttk.Scrollbar(m, command=contenidoTexto.yview) #Lo añadimos al contenidoTexto y le decimos que sea vertical
        #pero con esto no es suficiente, por esto tenemos que colocarlo con grid
        #vamos a cambiar el tamaño del scroll                                   
        scrollVert.grid(column=4, row=7, sticky="nsew", padx=5, pady=5)         
        # agregar posicionamiento del scroll según donde nos encontramos en la área del texto
        contenidoTexto.config(yscrollcommand=scrollVert.set)                    
                                                                                
        contenidoTexto.insert(INSERT, resultado)                                
        contenidoTexto.get("1.0", "end")                                        
        contenidoTexto.configure(state=DISABLED)                                
                                                                                
        #except subprocess.TimeoutExpired:                                           
        #    createFile.kill()   

def window_mirror_list():
    global root
    root = Tk() # creando el contenedor de la ventana
    root.title("Create Archlinux mirrorlist")
    root.config(bg="lightgray")
    
    ## Aplicando el estilo de la ventana
    themes(root)

    ## Creando la barra de menu
    barraMenu = Menu(root, bg=themeColor.get())
    root.config(menu=barraMenu)
   
    ## apartado fichero
    file_menu = Menu(barraMenu, bg=themeColor.get(), tearoff=0) 
    barraMenu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=lambda: exit(0))

    ## apartado usuario
    bbdd_usuario_menu = Menu(barraMenu, bg=themeColor.get(), tearoff=0)
    barraMenu.add_cascade(label="User", menu=bbdd_usuario_menu)
    bbdd_usuario_menu.add_command(label="Update password", command=lambda: window_create_user(True))
    bbdd_usuario_menu.add_command(label="Remove user and close the app", command=lambda: deleteUser(usuario, root))


    ## Help menu
    help_menu = Menu(barraMenu, bg=themeColor.get(), tearoff=0)
    barraMenu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    # Creando la ventana
    MyFrame = Frame(root)
    MyFrame.config(padx=10, pady=10, bg=themeColor.get())
    MyFrame.pack()
    
    paisLabel = ttk.Label(MyFrame, text="Select new country: ")
    paisLabel.grid(column=1, columnspan=4, sticky="w", row=1, padx=230, pady=10)

    country = StringVar()
    country.set("All")
    mirrorlist_countries = countries()
    mirrorlist_countries.insert(0, country.get())
    #countryBox = ttk.Entry(MyFrame, textvariable=country)
    #countryBox.grid(column=1, row=2, columnspan=4, padx=10, pady=10)
    #countryBox.config(background="white")

    select_countries = ttk.Combobox(MyFrame, textvariable=country)
    select_countries.grid(column=1, row=2, columnspan=4, padx=10, pady=10)
    select_countries['values'] = mirrorlist_countries
    select_countries['state'] = 'readonly'

    passwdLabel = ttk.Label(MyFrame, text="Put your user password: ")
    passwdLabel.grid(column=1, columnspan=4, sticky="w", row=3, padx=230, pady=5)

    passwd = StringVar()
    passwdBox = ttk.Entry(MyFrame, textvariable=passwd)
    passwdBox.grid(column=1, row=4, columnspan=4, padx=10, pady=10)
    passwdBox.config(background="white", show="*")

    Buton = ttk.Button(MyFrame, text="Create mirrorlist", command=lambda:createFile(country.get(), passwd.get(), MyFrame))
    Buton.grid(column=1, row=5, columnspan=1, padx=10, pady=10)
    cancelButon = ttk.Button(MyFrame, text="Cancelar", command=lambda:close(root))                               
    cancelButon.grid(column=2, row=5, columnspan=1, padx=10, pady=10) 

    contenidoTexto = Text(MyFrame, state=NORMAL, height=15, bg=themeColor.get(), highlightthickness=0, borderwidth=0)
    contenidoTexto.grid(column=1, columnspan=3, row=7, sticky="e", padx=10, pady=10)
    #contenidoTexto.delete("1.0", "end")
    contenidoTexto.get("1.0", "end")
    contenidoTexto.configure(state=DISABLED)


    root.mainloop()                                                                 

window_mirror_list()
