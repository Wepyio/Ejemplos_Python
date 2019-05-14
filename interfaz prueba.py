#probando tkinter
import time
import Tkinter as T
#from Tkinter import *

def ingreso():
    v1.deiconify()
    
v = T.Tk()
v.title('Telefonia')
saludo = T.Label(v, text = 'Bienvenido a Telefonia 980')
saludo.grid(row = 1, column = 1)
kase = ''
texto = T.Entry(v, textvariable = kase)
texto.grid(row = 1, column = 2)
v.config(bg = 'gray')
v.geometry('640x480')
v1 = T.Toplevel(v)
v1.title('Datos')
v1.withdraw()
entrar = T.Button(v, text = 'Entrar', command = lambda: ingreso())
entrar.grid(row = 2, column = 2)
#v1.withdraw() #oculta la ventana
#v1.deiconify() #muestra la ventana
v.mainloop()
