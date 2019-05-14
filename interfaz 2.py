#probando tkinter
import time
import Tkinter as T
#import Tkinter2 as T2
#import int_datos
#from Tkinter import *

global a

class parcial(object):

    def __init__(self):
        self.ingreso = T.Tk()
        self.ingreso.title('Telefonia')
        self.ingreso.geometry('440x320')
        #self.ingreso.config(bg = 'black')
        self.datos = T.Toplevel()
        self.datos.title('Datos de Usuario')
        self.datos.geometry('400x440')
        #self.datos.config(bg = 'gray')
        self.sistema = T.Tk()
        self.sistema.title('Identificador de Numeros Telefonicos')
        self.sistema.geometry('480x320')
        #self.sistema.config(bg = 'gray')

    def inicio(self, u = 0, c = 0):
        img = T.PhotoImage(file = 'logo.gif')
        imaje = T.Label(self.ingreso, image = img)
        imaje.grid(row = 1, column = 1)

        User = T.Label(self.ingreso, text = 'Usuario:')
        User.grid(row = 2, column = 2)
        user = T.Entry(self.ingreso)
        user.grid(row = 2, column = 3)
        Pass = T.Label(self.ingreso, text = 'Clave:')
        Pass.grid(row = 3, column = 2)
        passw = T.Entry(self.ingreso)
        passw.grid(row = 3, column = 3)
        entrar = T.Button(self.ingreso, text = 'Entrar', command = lambda: self.revisar(user,passw))
        entrar.grid(row = 4, column = 3)

        #self.datos.mainloop()
        self.datos.withdraw()
        self.sistema.withdraw()
        self.ingreso.mainloop()

    def revisar(self, user, passw, flag = 0):
        u = user.get()
        c = passw.get()
        
        login = open('login.txt', 'r')
        for i in login:
            if i == u+','+c+'\n':
                flag = 1
                #int_datos.ventana()
                self.usuario()

        if flag == 0:
            Fail = T.Label(self.ingreso, text = 'Datos Incorrectos', fg = 'black')
            Fail.grid(row = 5, column = 3)
            
        else:
            Fail = T.Label(self.ingreso, text = 'Datos Incorrectos', fg = 'white')
            Fail.grid(row = 5, column = 3)
            
        login.close()
        
        entrada = open('login.txt', 'r')
        entrada.close()
        
    def usuario(self):

        #self.ingreso.withdraw()
        #self.ingreso.wait_window(self.datos)
        
        nombre = T.Label(self.datos, text = 'Nombre Completo:')
        nombre.grid(row = 1, column = 1)
        name = T.Entry(self.datos)
        name.grid(row = 1, column = 2)
        
        usuario = T.Label(self.datos, text = 'Nombre de Usuario:')
        usuario.grid(row = 2, column = 1)
        user = T.Entry(self.datos)
        user.grid(row = 2, column = 2)
        
        correo = T.Label(self.datos, text = 'Correo:')
        correo.grid(row = 3, column = 1)
        mail = T.Entry(self.datos)
        mail.grid(row = 3, column = 2)
        
        edad = T.Label(self.datos, text = 'Edad:')
        edad.grid(row = 4, column = 1)
        age = T.Entry(self.datos)
        age.grid(row = 4, column = 2)
        
        clave = T.Label(self.datos, text = 'Clave:')
        clave.grid(row = 5, column = 1)
        passw = T.Entry(self.datos)
        passw.grid(row = 5, column = 2)

        foto = T.Label(self.datos, text = 'Foto:')
        foto.grid(row = 6, column = 1)
        f = T.PhotoImage(file = 'usuario.gif')
        photo = T.Label(self.datos, image = f)
        photo.grid(row = 6, column = 2)
        
        guardar = T.Button(self.datos, text = 'Guardar', command = lambda: self.nuevo(name,user,mail,age,passw))
        guardar.grid(row = 7, column = 2)
        
        self.datos.deiconify()
        #self.datos.mainloop()
        #self.datos.deiconify()
        self.ingreso.wait_window(self.datos)

    def nuevo(self, name, user, mail, age, passw):
        n = name.get()
        u = user.get()
        m = mail.get()
        a = age.get()
        p = passw.get()
        
        if (n != '' and u != '' and m != '' and a != '' and p != ''): #revisa que todos los campos esten llenos
            login = open('login.txt', 'r')
            Failc = T.Label(self.datos, text = 'Falta Llenar Algunos Campos', fg = 'white')
            Failc.grid(row = 8, column = 2)
            for i in login:
                if u in i:# revisa si ya existe este nombre de usuario
                    Failu = T.Label(self.datos, text = 'Este Usuario ya Existe', fg = 'black')
                    Failu.grid(row = 2, column = 3)

                else:
                    Failu = T.Label(self.datos, text = 'Este Usuario ya Existe', fg = 'white')
                    Failu.grid(row = 2, column = 3)
                    try:# revisa si se ingresa un numero
                        int(a)
                        Faila = T.Label(self.datos, text = 'Ingrese una Edad', fg = 'white')
                        Faila.grid(row = 4, column = 3)
                        usuarios = open('usuarios.txt','a')
                        usuarios.write(n+','+u+','+m+','+a+','+p+'\n')
                        usuarios.close()
                        #Faila.withdraw()
                    except ValueError:
                        Faila = T.Label(self.datos, text = 'Ingrese una Edad', fg = 'black')
                        Faila.grid(row = 4, column = 3)

            login.close()

        else:
            Failc = T.Label(self.datos, text = 'Falta Llenar Algunos Campos', fg = 'black')
            Failc.grid(row = 8, column = 2)
        
    def servicio(self):
        self.sistema.deiconify()

def run():
    try:
        p = parcial()
        p.inicio()

    except SystemError:
        print 'error shabo'

    except KeyboardInterrupt:
        print 'cerrado shabo'
        
run()
