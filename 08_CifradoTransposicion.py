claro = input('Mensaje a cifrar? ')
columnas = int(input('Cuantas columnas? '))
codificado = ''
claro = claro.replace(' ','') # Se eliminan los espacios
claro = claro.upper()         # Se pasa a mayusculas
renglones = int(len(claro)/columnas)+1
papel = [['' for x in range(columnas)] for x in range(renglones)]
claro = claro + 'X' * (renglones*columnas - len(claro))
k=0
for i in range(renglones):
    for j in range(columnas):
        papel[i][j]=claro[k]
        print(papel[i][j],end = ' ')
        k+=1
    print()
for j in range(columnas):
    for i in range(renglones):
        codificado=codificado + papel[i][j]
print('Texto en claro:',claro)
print('Texto codificado:', codificado)
