from random import randint
import math
def Cifrar(claro):
    E = claro.rfind(' ')
    columnas=int(claro[E+1:len(claro)-1])
    codificado=''
    claro = claro.replace(' ','') # Se eliminan los espacios
    claro = claro.upper() # Se pasa a mayusculas
    renglones=int(math.ceil(len(claro)/float(columnas)))
    papel = [['' for x in range(columnas)] for y in range(renglones)]
    claro=claro + '*' * (renglones*columnas - len(claro))
    k=0
    for i in range(renglones):
        for j in range(columnas):
            papel[i][j]=claro[k]
            k+=1
    for j in range(columnas):
        for i in range(renglones):
            codificado=codificado + papel[i][j]
    return codificado
z = 4 # Id del Mensaje
k = 18 # Digitos de la llave
N = 100 #Numero de mensajes
X = [[randint(0,9) for i in range(z)]for i in range(N)]
Y = [[randint(0,9) for i in range(k)]+[randint(3,18)] for i in range(N)]
S = ['Mensaje No. '+str(X[i]).replace(',','') + ' y su llave es'+str(Y[i]).replace(',','') for i in range(N)]
C = [Cifrar(S[i]) for i in range(N)]
archivo=open('MerkleTS.txt','w')
for i,s in enumerate(S):
    archivo.write(str(i)+','+s+'\n')
archivo.close()
archivo=open('MerkleTC.txt','w')
for c in C:
    archivo.write(c+'\n')
archivo.close()
print('Se generaron %d mensajes con la estructura:' % N)
print(S[0])
print('Se generaron los mensajes simples en MerkleTS.txt')
print('Se generaron los mensajes cifrados en MerkleTC.txt')
