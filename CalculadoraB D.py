#Proyectos 2S17
import psycopg2, psycopg2.extras

class Calculadora(object):
    
    def __init__(self):
        self.ope = 0
        self.n1 = 0
        self.n2 = 0
        self.answer = 0
        
    def Inicio(self):
        print '\nBienvenido a la Calculadora con Base de Datos'
        print 'Suma (s), Resta (r), Multiplicacion(m), Division(d), Para Borrar Base de Datos (b)'
        while(1):
            self.ope = raw_input('Que Operacion Desea Realizar?  ')
            if (self.ope == 's' or self.ope == 'r' or self.ope == 'm' or self.ope == 'd' or self.ope == 'b'):
                break
        
        if self.ope != 'b':
            while(1):
                self.n1 = raw_input('\nIngrese n1 -->  ')    
                try:
                    float(self.n1)
                    break
                except ValueError:
                    print '\nIngrese un Valor Numerico'      
                    
            while(1):
                self.n2 = raw_input('\nIngrese n2 -->  ')    
                try:
                    float(self.n2)
                    if (float(self.n2) == 0.0 and self.ope == 'd'):
                        print '\n El Resultado es Indefinido'
                    else:
                        break
                except ValueError:
                    print '\nIngrese un Valor Numerico'      
                    
            self.Operacion()
        else:
            self.Borrado()
        
    def Operacion(self):
        if self.ope == 's':
            self.answer = float(self.n1) + float(self.n2)
        elif self.ope == 'r':
            self.answer = float(self.n1) - float(self.n2)
        elif self.ope == 'm':
            self.answer = float(self.n1) * float(self.n2)
        elif self.ope == 'd':
            self.answer = float(self.n1) / float(self.n2)
        
        print self.answer

        self.Base()
        
    def Base(self):
        
        conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')
        cur = conn.cursor()
        cur.execute("INSERT INTO calcu (n1, operador, n2, answer) VALUES ('"+str(self.n1)+"','"+str(self.ope)+"','"+str(self.n2)+"','"+str(self.answer)+"')")
        conn.commit()
        conn.close()
    
    def Borrado(self):
        conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')
        cur = conn.cursor()
        cur.execute("DELETE FROM calcu")
        conn.commit()
        conn.close()
        
        print '\nBase de Datos Borrada\n'
        
def run():
    while(1):
        try:
            c = Calculadora()
            c.Inicio()
        except KeyboardInterrupt:
            break
            #break
        
run()
