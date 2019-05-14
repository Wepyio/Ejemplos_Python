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
        print 'Suma (s), Resta (r), Multiplicacion(m), Division(d)'
        while(1):
            self.ope = raw_input('Que Operacion Desea Realizar?  ')
            if (self.ope == 's' or self.ope == 'r' or self.ope == 'm' or self.ope == 'd'):
                break
        
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
        cur.execute("SELECT * FROM estudiante")
        rows=cur.fetchall()
        print rows
        
def run():
    while(1):
        try:
            c = Calculadora()
            c.Inicio()
        except KeyboardInterrupt:
            break
        
run()