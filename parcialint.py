# -*- coding: utf-8 -*-
import guarda
import base64
import sys
import psycopg2, psycopg2.extras
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
from PyQt4.QtCore import SIGNAL, QString, QEvent
from PyQt4.QtGui import (QApplication, QHBoxLayout, QIcon, QMainWindow,
                         QLabel, QLineEdit, QPushButton, QTreeWidget,
                         QTreeWidgetItem, QVBoxLayout, QWidget, QPixmap,
                         QMessageBox, QDialog)

global a 

a = []

class menu(QDialog):

    def __init__(self):

        super(menu, self).__init__(None)
        
        self.resize(400, 270)
        self.setWindowTitle('Menu Principal')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(160,20,216,233)
        self.imaje.setPixmap(QPixmap(getcwd()+"/menu.png"))
        
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
        
        self.connect(self.agr_usr, SIGNAL('clicked()'), lambda: self.hacer(nuevousuario()))
        self.connect(self.serv_tel, SIGNAL('clicked()'), lambda: self.hacer(revisarnumeros()))
        self.connect(self.usar, SIGNAL('clicked()'), lambda: self.hacer(reporte()))
        self.connect(self.acde, SIGNAL('clicked()'), lambda: self.hacer(about()))        
        self.connect(self.slir, SIGNAL('clicked()'), lambda: self.hacer(orale()))
        
    def hacer(self, i):
		e = i
		e.exec_()
		        				
class nuevousuario(QDialog):

    def __init__(self):

        super(nuevousuario, self).__init__(None)
        self.foto = ''
        self.resize(400, 460)
        self.setWindowTitle('Datos de Usuario')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(160,210,225,225)
        self.imaje.setPixmap(QPixmap("usuario.png"))
        
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

        key = self.Pass
        key.setEchoMode(self.Pass.Password)
        
        self.buscarfoto = QPushButton('Buscar Foto', self)
        self.buscarfoto.setGeometry(10, 250, 100, 30)
        
        self.guardar = QPushButton('Guardar', self)
        self.guardar.setGeometry(30, 300, 60, 30)

        self.failc = QLabel('Llenar Campos Vacios',self)
        self.failc.move(10,350)
        self.failc.hide()

        self.failf = QLabel('Elija Una Foto',self)
        self.failf.move(140,440)
        self.failf.hide()
                
        self.connect(self.buscarfoto, SIGNAL('clicked()'), lambda: self.buscar(self.ponfoto))
        self.connect(self.guardar, SIGNAL('clicked()'), lambda: self.nuevo(self.Name, self.User, self.Mail, self.Age, self.Pass))
        #sys.exit(self.editar.exec_())

    def buscar(self, do):
        e = explorador(do)
        e.exec_()		

    def ponfoto(self, a):
        self.foto = a		
        self.imaje.setPixmap(QPixmap(a))
        #self.show()
        		
    def nuevo(self, name, user, mail, age, passw, pe = 0):
        n = name.text()
        u = user.text()
        m = mail.text()
        a = age.text()
        p = passw.text()
        flag = 0
        if (n != '' and u != '' and m != '' and a != '' and p != ''): #revisa que todos los campos esten llenos
            login = open('login.txt', 'r')
            self.failc.hide()
            
            for i in login:
                if str(u) in i:# revisa si ya existe este nombre de usuario
                    self.failu.show()
                    flag = 0

                else:
                    self.failu.hide()
                    flag = 1

            login.close()
            
            if flag == 1:
                try:# revisa si se ingresa un numero
                    int(a)
                    self.faila.hide()
                    o = self.passcheck(str(p))
                    if o == 1:
                        self.failp.hide()
                        pe = base64.b64encode(str(p))
                        #if self.foto != '':

                        guarda.guardar(n,u,m,a,pe)
                                                        
                        conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')
                        cur = conn.cursor()
                        cur.execute("INSERT INTO usuarios (nombre, usuario, correo, edad, clave) VALUES ('"+n+"','"+u+"','"+m+"','"+a+"','"+pe+"');")
                        conn.commit()
                        conn.close()

                        usuarios = open('usuarios.txt','a')
                        usuarios.write(n+','+u+','+m+','+a+','+pe+','+self.foto+',\n')
                        usuarios.close()
                        self.failf.hide()
                        #break
                        #else:
                        #    self.failf.show()
                    else:
                        self.failp.show() 							
                except ValueError:
                    self.faila.show()


        else:
            self.failc.show()
        
    def passcheck(self, clave, f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0, minimo = 6, flag = 0):
        for i in clave:
            n = ord(i)
            if (n >= 0 and n < 48): #simbolos
                f1 = 1
            elif (n >= 48 and n < 58): #numeros
                f2 = 1
            elif (n >= 58 and n < 65): #simbolos
                f1 = 1
            elif (n >= 65 and n < 91): #mayusculas
                f3 = 1
            elif (n >= 91 and n < 97): #simbolos
                f1 = 1
            elif (n >= 97 and n < 123): #minus
                f4 = 1
            elif (n == 209):
                f3 = 1
            elif (n == 241):
                f4 = 1
            elif (n >= 123 and n < 256): #simbolos
                f1 = 1

        if len(clave) >= minimo:
            f5 = 1

        if (f1*f2*f3*f4*f5 == 1):
            flag = 1
        else:
            flag = 0
        return flag
            
class revisarnumeros(QDialog):

    def __init__(self):

        super(revisarnumeros, self).__init__(None)
        
        #self.d = ''
        self.resize(340, 240)
        self.setWindowTitle('Servicio de Telefonia')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(120,10,225,225)
        self.imaje.setPixmap(QPixmap("tele.png"))
        
        self.buscararchivo = QPushButton('Buscar Archivo', self)
        self.buscararchivo.setGeometry(10, 10, 100, 30)
        
        self.revisar = QPushButton('Revisar', self)
        self.revisar.setGeometry(30, 60, 60, 30)

        self.connect(self.buscararchivo, SIGNAL('clicked()'), lambda: self.buscar(self.analizar))
        self.connect(self.revisar, SIGNAL('clicked()'), lambda: self.ver())

    def buscar(self, do):
        e = explorador(do)
        e.exec_()		
		#self.d = e.exec_()
		#print self.d

    def analizar(self, doc):
		l = listado(doc)
		l.ingreso()
		
    def ver(self):	
        startfile(a[len(a)-1])		
        """salida = open(a[len(a)-1], 'rU')
        for i in salida:
			print i
        salida.close()			
        #v = vista()
        #v.exec_()
        """		
class reporte(QDialog):

    def __init__(self):

        super(reporte, self).__init__(None)
        
        self.resize(340, 240)
        self.setWindowTitle('Realizar Reporte')
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(120,10,225,225)
        self.imaje.setPixmap(QPixmap("tele.png"))
        
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
        self.imaje.setPixmap(QPixmap("proyecto.png"))
        
        self.n = QLabel('Proyectos 980 \nGrupo 2 \n\nIntegrantes: \n\nJason Hernandez \t201020518 \nChristian Flores \t\t201212650 \nHasler Herrera \t\t201046499 \nDennis Conde \t\t201245425 \nCarlos Salcedo \t\t201020527 \nSamuel Choc \t\t201318619',self)
        self.n.move(10,10)

        #self.guardar = QPushButton('Revisar', self)
        #self.guardar.setGeometry(30, 60, 60, 30)

class orale(QDialog):

    def __init__(self):

        super(orale, self).__init__(None)
        
        self.resize(245, 300)
        self.setWindowTitle('Saliendo de Telefonia')

        self.p = QLabel('Desea Cerrar el Programa?',self)
        self.p.move(10,10)
        
        self.imaje = QLabel(self)
        self.imaje.setGeometry(10,60,225,225)
        self.imaje.setPixmap(QPixmap("duda.png"))
        
        self.salirsi = QPushButton('Si', self)
        self.salirsi.setGeometry(60, 30, 60, 30)
        
        self.salirno = QPushButton('No', self)
        self.salirno.setGeometry(125, 30, 60, 30)

        self.connect(self.salirsi, SIGNAL('clicked()'), lambda: self.salir())
        self.connect(self.salirno, SIGNAL('clicked()'), lambda: self.close())

    def salir(self):
		exit()
		
class parcial(QWidget):

    def __init__(self):
        
        self.ingresar = QApplication(sys.argv)
        super(parcial, self).__init__(None)
        self.contador = 0
        self.ingreso = QWidget()
        self.ingreso.resize(440, 320)
        self.ingreso.setWindowTitle('Autenticacion de Ingreso')
        
        self.sistema = QWidget()
        self.sistema.resize(480, 320)
        self.sistema.setWindowTitle('Identificador de Numeros Telefonicos')

    def inicio(self, u = 0, c = 0):
        
        self.imaje = QLabel(self.ingreso)
        self.imaje.setGeometry(10,10,225,225)
        self.imaje.setPixmap(QPixmap("logo.png"))
        
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
        key = self.Pass
        key.setEchoMode(self.Pass.Password)
        
        self.entra = QPushButton('Entrar', self.ingreso)
        self.entra.setGeometry(320, 260, 60, 30)
        
        self.ingreso.connect(self.entra, SIGNAL('clicked()'), lambda: self.revisar(self.User, self.Pass))
        
        self.ingreso.show()
        
        sys.exit(self.ingresar.exec_())
        
        
    def revisar(self, user, passw, flag = 0):
        
        u = user.text()
        c = passw.text()
        ce = base64.b64encode(str(c))

        login = open('usuarios.txt', 'rU')
        for i in login:
            n = i.split(',')

            if (n[1] == u and n[4] == ce):
                flag = 1
                self.m.hide()
                m = menu()
                m.exec_()
                break
            elif (n[1] == u and n[4] != ce):
                self.contador += 1
                flag = 0
                self.m.show()
                if self.contador == 3:
                    bloqueado = open('bloqueados.txt', 'a')
                    bloqueado.write(i)
                    bloqueado.close()
        if flag == 0:
            self.m.show()
        
        d = strftime('%d/%m/%y')
        h = strftime('%H:%M:%S')
                            		
        conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')
        cur = conn.cursor()
        cur.execute("INSERT INTO accesos (nombre, usuario, fecha, hora) VALUES ('"+n[0]+"','"+n[1]+"','"+d+"','"+h+"')")
        conn.commit()
        conn.close()

        login.close()
        entrada = open('ingreso.txt', 'a')
        entrada.write('Ha Ingresado '+n[1]+' Hoy '+d+' a las '+h+'\n')
        entrada.close()

class explorador(QDialog):
    
    def __init__(self, accion):
        self.a = 0
        self.do = accion
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
            self.do(filepath)
            self.close()
                
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

class listado(object):

    def __init__(self, o):
        self.claro = [[5010,5019],[5110,5139],[5410,5499],[5510,5517],[5560,5579],[5582,5599],[5610,5639],[5690,5699],[5710,5718],[5810,5818],[5820,5879],[5910,5914],[5920,5989]] #Cada lista contiene el maximo y minimo de cada rango
        self.movistar = [[5020,5029],[5070,5109],[5140,5149],[5210,5299],[5390,5409],[5500,5509],[5600,5608],[5640,5699]]
        self.tigo = [[5000,5009],[5030,5069],[5150,5209],[5300,5309],[5314,5389],[5521,5529],[5550,5553],[5580,5581],[5700,5709],[5720,5789],[5800,5809],[5880,5909],[5918,5919],[5990,5999]]
        self.o = o
        self.s = 0

    def ingreso(self): #Solo ingresar el numero, la extension se agrega aca
        
        try:
            entrada = open(self.o, 'r')
            
        except IOError:
            None

        for e in entrada:

            try:
                n = int(e)/10000
                if (n < 10000 or n < 2000):
                    self.revisar(n, e)
                else:
                    print '\nLa Linea --> '+e+' no Contiene un Numero Telefonico de 8 Digitos\n'
                
            except ValueError:
                print '\nLa Linea --> '+e+' no Contiene un Numero Telefonico\n'
            
        entrada.close()
        
    def revisar(self, n = 0, e = 0): #Aca se verifica a que compania pertenece el numero
        h = strftime('%d-%m-%y-%H_%M_%S')		
        salida = open('revisado'+h+'.csv', 'a')
        a.append('revisado'+h+'.csv')
        for i in self.claro:
            if (n >= i[0] and n <= i[1]):
                salida.write('Claro,')
                salida.write(e+',')
                #print e+' es claro'
        for i in self.movistar:
            if (n >= i[0] and n <= i[1]):
                salida.write('Movistar,')
                salida.write(e+',')
                #print e+' es movistar'
        for i in self.tigo:
            if (n >= i[0] and n <= i[1]):
                salida.write('Tigo,')
                salida.write(e+',')
                #print e+' es tigo'
        salida.close()
                
def run():
    try:
        p = parcial()
        p.inicio()
        
    except SystemError:
        print 'error shabo'

    except KeyboardInterrupt:
        print 'cerrado shabo'
        
run()
