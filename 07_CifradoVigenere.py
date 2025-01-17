claro = input('Mensaje a cifrar? ')
clave = input('Clave? ')
tabla = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codificado = ''
claro = claro.replace(' ','') # Se eliminan los espacios
claro = claro.upper()         # Se pasa a mayusculas
clave = clave.upper()         # Se pasa a mayusculas

d = len(clave)

i = 0
for m in claro:
     codificado = codificado + tabla[(tabla.find(m)+(tabla.find(clave[i%d])))%26]
     i=i+1

print('Texto en claro: ',claro)
print('Texto cifrado:  ',codificado)
