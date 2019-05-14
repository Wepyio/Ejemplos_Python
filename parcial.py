# -*- coding: utf-8 -*-

import Tkinter as T
import sys
import pg
from os import getcwd, listdir, stat
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime, sleep
try:
    # Windows.
    from os import startfile
except ImportError:
    # Otras plataformas.
    from webbrowser import open as startfile
from hurry.filesize import size
from PyQt4.QtCore import SIGNAL, QString
from PyQt4.QtGui import (QApplication, QHBoxLayout, QIcon, QMainWindow,
                         QLabel, QLineEdit, QPushButton, QTreeWidget,
                         QTreeWidgetItem, QVBoxLayout, QWidget, QPixmap,
                         QMessageBox, QDialog)

global a

class menu(QDialog):

    def __init__(self):

        super(menu, self).__init__(None)
        
        self.resize(400, 270)
        self.setWindowTitle('Menu Principal')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(160,20,216,233)
        self.imaje.setPixmap(QPixmap(getcwd()+"/menu.jpeg"))
        
        self.agr_usr = QPushButton('Agregar Usuario', self)
        self.agr_usr.setGeometry(20, 20, 120, 30)
        
        self.serv_tel = QPushButton('Revisar Telefonos', self)
        self.serv_tel.setGeometry(20, 70, 120, 30)
        
        self.usar = QPushButton('Realizar Reporte', self)
        self.usar.setGeometry(20, 120, 120, 30)
        
        self.acde = QPushButton('Acerca de', self)
        self.acde.setGeometry(20, 170, 120, 30)
        
        self.slir = QPushButton('Salir', self)
        self.slir.setGeometry(20, 220, 120, 30)
        
        self.connect(self.agr_usr, SIGNAL('clicked()'), lambda: self.hacer(entrar()))
        self.connect(self.serv_tel, SIGNAL('clicked()'), lambda: self.hacer(mostrar()))
        self.connect(self.usar, SIGNAL('clicked()'), lambda: self.hacer(reporte()))
        self.connect(self.acde, SIGNAL('clicked()'), lambda: self.hacer(about()))        
        self.connect(self.slir, SIGNAL('clicked()'), lambda: self.hacer(orale()))
        
    def hacer(self, i):
		e = i
		e.exec_()
		        				
class entrar(QDialog):

    def __init__(self):

        super(entrar, self).__init__(None)
        
        self.resize(400, 440)
        self.setWindowTitle('Datos de Usuario')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(160,210,225,225)
        self.imaje.setPixmap(QPixmap(getcwd()+"/usuario.gif"))
        
        self.n = QLabel('Nombre Completo:',self)
        self.n.move(10,10)
        
        self.u = QLabel('Nombre de Usuario:',self)
        self.u.move(10,50)
        
        self.failu = QLabel('Este Usuario ya Existe',self)
        self.failu.move(140,70)
        self.failu.hide()
        
        self.c = QLabel('Correo Electronico:',self)
        self.c.move(10,90)
        
        self.a = QLabel('Edad:',self)
        self.a.move(10,130)
  
        self.faila = QLabel('Ingrese una Edad',self)
        self.faila.move(140,150)
        self.faila.hide()
      
        self.p = QLabel('Clave:',self)
        self.p.move(10,170)
        
        self.failp = QLabel('Clave muy Debil',self)
        self.failp.move(140,190)
        self.failp.hide()

        self.f = QLabel('Foto:',self)
        self.f.move(10,210)
        
        self.Name = QLineEdit(self)
        self.Name.setGeometry(140, 10, 200, 20)
        
        self.User = QLineEdit(self)
        self.User.setGeometry(140, 50, 200, 20)
        
        self.Mail = QLineEdit(self)
        self.Mail.setGeometry(140, 90, 200, 20)
        
        self.Age = QLineEdit(self)
        self.Age.setGeometry(140, 130, 200, 20)
        
        self.Pass = QLineEdit(self)
        self.Pass.setGeometry(140, 170, 200, 20)
        
        self.buscarfoto = QPushButton('Buscar Foto', self)
        self.buscarfoto.setGeometry(10, 250, 100, 30)
        
        self.guardar = QPushButton('Guardar', self)
        self.guardar.setGeometry(30, 300, 60, 30)

        self.failc = QLabel('Llenar Campos Vacios',self)
        self.failc.move(10,350)
        self.failc.hide()
                
        self.connect(self.buscarfoto, SIGNAL('clicked()'), lambda: self.buscar())
        self.connect(self.guardar, SIGNAL('clicked()'), lambda: self.nuevo(self.Name, self.User, self.Mail, self.Age, self.Pass))
        #sys.exit(self.editar.exec_())

    def ponfoto(self, a):
        self.imaje.hide()
        #self.imaje.setPixmap(QPixmap(a))		
        
    def buscar(self):
		e = explorador()
		e.exec_()
		
    def nuevo(self, name, user, mail, age, passw):
        n = name.text()
        u = user.text()
        m = mail.text()
        a = age.text()
        p = passw.text()
        
        if (n != '' and u != '' and m != '' and a != '' and p != ''): #revisa que todos los campos esten llenos
            login = open('login.txt', 'r')
            self.failc.hide()
            
            for i in login:
                if str(u) in i:# revisa si ya existe este nombre de usuario
                    self.failu.show()

                else:
                    self.failu.hide()

                    try:# revisa si se ingresa un numero
                        int(a)
                        self.faila.hide()
                        usuarios = open('usuarios.txt','a')
                        usuarios.write(n+','+u+','+m+','+a+','+p+'\n')
                        usuarios.close()
                        
                    except ValueError:
                        self.faila.show()

            login.close()

        else:
            self.failc.show()
        
class mostrar(QDialog):

    def __init__(self):

        super(mostrar, self).__init__(None)
        
        self.resize(340, 240)
        self.setWindowTitle('Servicio de Telefonia')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(120,10,225,225)
        self.imaje.setPixmap(QPixmap(getcwd()+"/tele.jpeg"))
        
        self.buscararchivo = QPushButton('Buscar Archivo', self)
        self.buscararchivo.setGeometry(10, 10, 100, 30)
        
        self.guardar = QPushButton('Revisar', self)
        self.guardar.setGeometry(30, 60, 60, 30)

class reporte(QDialog):

    def __init__(self):

        super(reporte, self).__init__(None)
        
        self.resize(340, 240)
        self.setWindowTitle('Realizar Reporte')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(120,10,225,225)
        self.imaje.setPixmap(QPixmap(getcwd()+"/tele.jpeg"))
        
        self.buscararchivo = QPushButton('Buscar Archivo', self)
        self.buscararchivo.setGeometry(10, 10, 100, 30)
        
        self.guardar = QPushButton('Revisar', self)
        self.guardar.setGeometry(30, 60, 60, 30)

class about(QDialog):

    def __init__(self):

        super(about, self).__init__(None)
        
        self.resize(560, 240)
        self.setWindowTitle('Acerca de')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(300,10,249,203)
        self.imaje.setPixmap(QPixmap(getcwd()+"/proyecto.jpeg"))
        
        self.n = QLabel('Proyectos 980 \nGrupo 2 \n\nIntegrantes: \n\nJason Hernandez \t201020518 \nChristian Flores \t\t201212650 \nHasler Herrera \t\t201046499 \nDennis Conde \t\t201245425 \nCarlos Salcedo \t\t201020527 \nSamuel Choc \t\t201318619',self)
        self.n.move(10,10)

        #self.guardar = QPushButton('Revisar', self)
        #self.guardar.setGeometry(30, 60, 60, 30)

class orale(QDialog):

    def __init__(self):

        super(orale, self).__init__(None)
        
        self.resize(340, 240)
        self.setWindowTitle('Servicio de Telefonia')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(120,10,225,225)
        self.imaje.setPixmap(QPixmap(getcwd()+"/tele.jpeg"))
        
        self.buscararchivo = QPushButton('Buscar Archivo', self)
        self.buscararchivo.setGeometry(10, 10, 100, 30)
        
        self.guardar = QPushButton('Revisar', self)
        self.guardar.setGeometry(30, 60, 60, 30)

class parcial(QWidget):

    def __init__(self):
        
        self.ingresar = QApplication(sys.argv)
        super(parcial, self).__init__(None)

        self.ingreso = QWidget()
        self.ingreso.resize(440, 320)
        self.ingreso.setWindowTitle('Autenticacion de Ingreso')
        
        self.sistema = QWidget()
        self.sistema.resize(480, 320)
        self.sistema.setWindowTitle('Identificador de Numeros Telefonicos')

    def inicio(self, u = 0, c = 0):
        
        self.imaje = QLabel(self.ingreso)
        self.imaje.setGeometry(10,10,225,225)
        self.imaje.setPixmap(QPixmap(getcwd()+"/logo.gif"))
        
        self.u = QLabel('Nombre de Usuario:',self.ingreso)
        self.u.move(288,162)
        
        self.c = QLabel('Clave:',self.ingreso)
        self.c.move(333,202)
        
        self.m = QLabel('Usuario y(o) Clave Incorrecta', self.ingreso)
        self.m.move(250,303)
        self.m.hide()
        
        self.User = QLineEdit(self.ingreso)
        self.User.setGeometry(280, 180, 140, 20)
        
        self.Pass = QLineEdit(self.ingreso)
        self.Pass.setGeometry(280, 220, 140, 20)
        
        self.entra = QPushButton('Entrar', self.ingreso)
        self.entra.setGeometry(320, 260, 60, 30)
        
        self.ingreso.connect(self.entra, SIGNAL('clicked()'), lambda: self.revisar(self.User, self.Pass))
        
        self.ingreso.show()
        
        sys.exit(self.ingresar.exec_())
        
        
    def revisar(self, user, passw, flag = 0):
        
        u = user.text()
        c = passw.text()
        #print u+''+c
        login = open('login.txt', 'rU')
        for i in login:
            if i == u+','+c+'\n':
                flag = 1
                self.m.hide()
                m = menu()
                m.exec_()

        if flag == 0:
            self.m.show()
            
            
        self.ingreso.update()
        login.close()
        
        #entrada = open('login.txt', 'r')
        #entrada.close()
                		
class explorador(QDialog):
    
    def __init__(self):
        self.a = 0
        super(explorador, self).__init__(None)
        self.setWindowTitle("Explorador de archivos y carpetas")
        self.resize(610, 450)
        
        self.back_history = []
        self.forward_history = []
        
        self.back = QPushButton('<-', self)
        self.back.clicked.connect(self.back_click)
        self.back.setGeometry(10, 10, 30, 20)
        self.back.setEnabled(False)

        self.forward = QPushButton('->', self)
        self.forward.clicked.connect(self.forward_click)
        self.forward.setGeometry(50, 10, 30, 20)
        self.forward.setEnabled(False)
        
        self.up = QPushButton('^', self)
        self.up.clicked.connect(self.up_button_click)
        self.up.setGeometry(90, 10, 30, 20)
        
        self.address = QLineEdit(self)
        self.address.setGeometry(130,10,420,20)
        
        self.refresh = QPushButton('@', self)
        self.refresh.clicked.connect(self.refresh_click)
        self.refresh.setGeometry(560, 10, 30, 20)
                        
        self.items = QTreeWidget(self)
        self.items.setRootIsDecorated(False)
        self.items.setHeaderLabels(
            ("Nombre", u"Fecha de modificación", u"Tamaño"))
        self.items.itemDoubleClicked.connect(self.item_double_clicked)
        self.items.setGeometry(5,40,600,400)        
        
        # Iniciar en el directorio actual.
        self.load_path(getcwd())
    
    def back_click(self, checked):
        if self.back_history and len(self.back_history) > 1:
            # Obtener el último elemento.
            path = self.back_history[-2]
            self.forward_history.append(self.back_history[-1])
            # Remover el directorio actual.
            del self.back_history[-1]
            self.load_path(path, False)
    
    def forward_click(self, checked):
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
            #print a
            e = entrar()
            e.ponfoto(a)
            #parcial.ponfoto(a)
            #print self.a
    
    def up_button_click(self, checked):
        parent = dirname(self.current_path)
        if parent != self.current_path:
            self.load_path(parent)
    
    def load_path(self, path, use_history=True):
        # Obtener archivos y carpetas.
        items = listdir(unicode(path))
        # Eliminar el contenido anterior.
        self.items.clear()
        
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
            self.items.addTopLevelItem(item_widget)
        
        # Ajustar el tamaño de las columnas.
        for i in range(3):
            self.items.resizeColumnToContents(i)
        
        self.current_path = path
        self.address.setText(self.current_path)
        
        # Añadir al historial.
        if use_history:
            self.back_history.append(self.current_path)
        
        # Habilitar / dehabilitar botones del historial.
        if self.back_history and len(self.back_history) > 1:
            if not self.back.isEnabled():
                self.back.setEnabled(True)
        else:
            if self.back.isEnabled():
                self.forward_history = []
                self.back.setEnabled(False)
        
        if self.forward_history:
            if not self.forward.isEnabled():
                self.forward.setEnabled(True)
        else:
            if self.forward.isEnabled():
                self.forward.setEnabled(False)
    
    def refresh_click(self, checked):
        self.load_path(self.current_path)
        
def run():
    try:
        p = parcial()
        p.inicio()
        
    except SystemError:
        print 'error shabo'

    except KeyboardInterrupt:
        print 'cerrado shabo'
        
run()
