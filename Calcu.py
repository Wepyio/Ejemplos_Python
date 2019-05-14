global a
global b

def suma(a,b):
    c = float(a) + float(b)
    print c

def resta(a,b):
    c = float(a) - float(b)
    print c

def multiplicacion(a,b):
    c = float(a) * float(b)
    print c

def division(a,b):
    c = float(a) / float(b)
    print c

def ingreso():
    while(1):
        a = raw_input('Ingrese el primer numero--->')
        try:
            int(a)
            break
        except:
            print '\nDebe ingresar numeros\n'

    while(1):
        b = raw_input('Ingrese el segundo numero-->')
        try:
            int(b)
            break
        except:
            print '\nDebe ingresar numeros\n'
    
def run():
    print 'Que operacion desea realizar?\n suma(s) \n resta(r) \n multiplicacion(m) \n division(d) \n'
    o = raw_input('\n--->')
    if o == 's':
        ingreso()
        suma(a,b)
    elif o == 'r':
        ingreso()
        resta(a,b)
    elif o == 'm':
        ingreso()
        multiplicacion(a,b)
    elif o == 'd':
        ingreso()
        division(a,b)
    else:
        run()

run()
