# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 15:10:13 2017

@author: User
"""

with open("nose.png", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

#print b

import base64

with open("nose.png", "rb") as imageFile:
    st = base64.b64encode(imageFile.read())
    b = bytearray(st)
    #print st
    
import psycopg2, psycopg2.extras
conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')

cur = conn.cursor()
cur.execute("INSERT INTO imagen (foto) VALUES ('"+str(b)+"');")
#rows=cur.fetchall()
#print rows
conn.commit()
conn.close()
"""

image = open('nose.png', 'rb')
bimage = bytearray(image)
image.close()
"""