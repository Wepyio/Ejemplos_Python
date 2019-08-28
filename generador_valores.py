#programa para generar la onda senoidal

import math

datos = []
#for(int i = 0; i <256; i++){
for i in range(256):
    #print i
    v = 0
    v = 128 + 127*(math.sin(i*((2*(math.pi))/256)))
    datos.append(int(v))
    #print str(int(v))

print datos
#delay(500);  time.sleep(0.5)
    
print 'adios'
