"""
login = open('login.txt','r')
    
for i in login:
    print i
    if i == 'sd\n':
        print 'si'
        

login.close()
"""
import Tkinter as T

v = T.Tk()
img = T.PhotoImage(file = 'logo.gif')
label1 = T.Label(v, image = img)
label1.grid(row = 1, column = 1)

v.mainloop()
