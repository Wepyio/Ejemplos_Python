
import Tkinter2 as T

def ventana():
    datos = T.Tk()
    datos.title('Datos de Usuario')
    datos.geometry('400x440')

    nombre = T.Label(datos, text = 'Nombre Completo:')
    nombre.grid(row = 1, column = 1)
    name = T.Entry(datos)
    name.grid(row = 1, column = 2)
    
    usuario = T.Label(datos, text = 'Nombre de Usuario:')
    usuario.grid(row = 2, column = 1)
    user = T.Entry(datos)
    user.grid(row = 2, column = 2)
    
    correo = T.Label(datos, text = 'Correo:')
    correo.grid(row = 3, column = 1)
    mail = T.Entry(datos)
    mail.grid(row = 3, column = 2)
    
    edad = T.Label(datos, text = 'Edad:')
    edad.grid(row = 4, column = 1)
    age = T.Entry(datos)
    age.grid(row = 4, column = 2)
    
    clave = T.Label(datos, text = 'Clave:')
    clave.grid(row = 5, column = 1)
    passw = T.Entry(datos)
    passw.grid(row = 5, column = 2)

    f = T.PhotoImage(file = 'usuario.gif')
    photo = T.Label(datos, image = f)
    photo.grid(row = 6, column = 2)

    datos.mainloop()
    
