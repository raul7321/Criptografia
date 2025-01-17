claro = input('Mensaje a cifrar: ')
tabla = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codificado = ''
claro = claro.replace(' ','') # Se eliminan los espacios
claro = claro.upper() # Se pasa a mayusculas
for m in claro:
    codificado = codificado + str(tabla.find(m)+11)
cifras=3
if len(codificado) %3!=0: cifras=2
print(claro,':', codificado)
A = [int(codificado[k:k+cifras]) for k in range(0,len(codificado),cifras)]
for i,k in enumerate(A):
    print ('a'+str(i) + ' = ' + str(k))
print ('Dame la llave publica (n,e)')
n = int(input('n = '))
e = int(input('e = '))
B=[a**e %n for a in A]
for i,k in enumerate(B):
    print ('b'+str(i) + ' = ' + str(k))
print ('Criptograma:', ','.join(map(str,B)))
