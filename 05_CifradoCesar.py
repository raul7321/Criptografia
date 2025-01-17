claro = input('Mensaje a cifrar? ')
clave = int(input('Clave? '))
tabla = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codificado = ''
claro = claro.replace(' ','') # Se eliminan los espacios
claro = claro.upper()         # Se pasa a mayusculas

for m in claro:
     codificado = codificado + tabla[(tabla.find(m)+clave)%26]

tabla_cifrado = ''.join([tabla[(tabla.find(m)+clave)%26] for m in tabla])

print('Tabla de cifrado:')

print(tabla)
print(tabla_cifrado)

print('Mensaje en claro:',claro)
print('Mensaje cifrado:',codificado)
