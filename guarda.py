# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 00:09:50 2017

@author: User

"""

import psycopg2

def guardar(n,u,m,a,pe):
    conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nombre, usuario, correo, edad, clave) VALUES ('"+n+"','"+u+"','"+m+"','"+a+"','"+pe+"')")
    conn.commit()
    conn.close()
