# -*- coding: utf-8 -*-
import Tkinter as T
import sys
from os import getcwd, listdir, stat
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime
try:
    # Windows.
    from os import startfile
except ImportError:
    # Otras plataformas.
    from webbrowser import open as startfile
from hurry.filesize import size
#from PyQt4.QtCore import QStringList
from PyQt4.QtGui import (QApplication, QHBoxLayout, QIcon, QMainWindow,
                         QLineEdit, QPushButton, QTreeWidget,
                         QTreeWidgetItem, QVBoxLayout, QWidget)

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
        
        explorar = T.Button(self.datos, text = 'Elegir Foto', command = lambda: self.buscar())
        explorar.grid(row = 7, column = 2)
        
        guardar = T.Button(self.datos, text = 'Guardar', command = lambda: self.nuevo(name,user,mail,age,passw))
        guardar.grid(row = 8, column = 2)
        
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
            Failc.grid(row = 9, column = 2)
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
            Failc.grid(row = 9, column = 2)
        
    def buscar(self):
        app = QApplication([])
        window = Window()
        window.show()
        sys.exit(app.exec_())
        
    def ponfoto(self, a):
        f = T.PhotoImage(file = a)
        photo = T.Label(self.datos, image = f)
        photo.grid(row = 6, column = 2)
        self.datos.update_idletasks()
        
    def servicio(self):
        self.sistema.deiconify()

class Window(QMainWindow):
    
    def __init__(self):
        self.a = 0
        QMainWindow.__init__(self)
        self.setWindowTitle("Explorador de archivos y carpetas")
        
        self.back_history = []
        self.forward_history = []
        
        self.back_button = QPushButton(self)
        self.back_button.setIcon(QIcon("images/back.png"))
        self.back_button.clicked.connect(self.back_clicked)
        self.back_button.setEnabled(False)
        
        self.forward_button = QPushButton(self)
        self.forward_button.setIcon(QIcon("images/forward.png"))
        self.forward_button.clicked.connect(self.forward_clicked)
        self.forward_button.setEnabled(False)
        
        self.up_button = QPushButton(self)
        self.up_button.setIcon(QIcon("images/up.png"))
        self.up_button.clicked.connect(self.up_button_clicked)
        
        self.address_edit = QLineEdit(self)
        
        self.refresh_button = QPushButton(self)
        self.refresh_button.setIcon(QIcon("images/update.png"))
        self.refresh_button.clicked.connect(self.refresh_button_clicked)
        
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.up_button)
        self.toplayout.addWidget(self.address_edit)
        self.toplayout.addWidget(self.refresh_button)
        
        self.main_tree = QTreeWidget(self)
        self.main_tree.setRootIsDecorated(False)
        self.main_tree.setHeaderLabels(
            ("Nombre", u"Fecha de modificación", u"Tamaño"))
        self.main_tree.itemDoubleClicked.connect(self.item_double_clicked)
        
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.main_tree)
        
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.resize(800, 600)
        # Iniciar en el directorio actual.
        self.load_path(getcwd())
    
    def back_clicked(self, checked):
        if self.back_history and len(self.back_history) > 1:
            # Obtener el último elemento.
            path = self.back_history[-2]
            self.forward_history.append(self.back_history[-1])
            # Remover el directorio actual.
            del self.back_history[-1]
            self.load_path(path, False)
    
    def forward_clicked(self, checked):
        if self.forward_history:
            path = self.forward_history[-1]
            self.back_history.append(path)
            del self.forward_history[-1]
            self.load_path(path, False)
    
    def item_double_clicked(self, item, column):
        filepath = join(self.current_path, unicode(item.text(0)))
        if isdir(filepath):
            self.load_path(filepath)
        else:
            # Iniciar archivo con el programa predeterminado.
            #startfile(filepath)
            
            a = filepath
            parcial.ponfoto(a)
            #print self.a
    
    def up_button_clicked(self, checked):
        parent = dirname(self.current_path)
        if parent != self.current_path:
            self.load_path(parent)
    
    def load_path(self, path, use_history=True):
        # Obtener archivos y carpetas.
        items = listdir(unicode(path))
        # Eliminar el contenido anterior.
        self.main_tree.clear()
        
        for i in items:
            # Omitir archivos ocultos.
            if i.startswith("."):
                continue
            filepath = join(path, i)
            # Obtener informacion del archivo.
            stats = stat(filepath)
            # Crear el control ítem.
            item_widget = QTreeWidgetItem(
                (i, strftime("%c", localtime(stats.st_mtime)).decode("utf-8"),
                 size(stats.st_size) if isfile(filepath) else "")
            )
            # Establecer el ícono correspondiente.
            item_widget.setIcon(0, QIcon("images/%s.png" %
                ("file" if isfile(filepath) else "folder")))
            # Añadir elemento.
            self.main_tree.addTopLevelItem(item_widget)
        
        # Ajustar el tamaño de las columnas.
        for i in range(3):
            self.main_tree.resizeColumnToContents(i)
        
        self.current_path = path
        self.address_edit.setText(self.current_path)
        
        # Añadir al historial.
        if use_history:
            self.back_history.append(self.current_path)
        
        # Habilitar / dehabilitar botones del historial.
        if self.back_history and len(self.back_history) > 1:
            if not self.back_button.isEnabled():
                self.back_button.setEnabled(True)
        else:
            if self.back_button.isEnabled():
                self.forward_history = []
                self.back_button.setEnabled(False)
        
        if self.forward_history:
            if not self.forward_button.isEnabled():
                self.forward_button.setEnabled(True)
        else:
            if self.forward_button.isEnabled():
                self.forward_button.setEnabled(False)
    
    def refresh_button_clicked(self, checked):
        self.load_path(self.current_path)
        
"""        
#if __name__ == "__main__":
def run():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())
    
run()
"""
def run():
    try:
        p = parcial()
        p.inicio()
        
    except SystemError:
        print 'error shabo'

    except KeyboardInterrupt:
        print 'cerrado shabo'
        
run()
