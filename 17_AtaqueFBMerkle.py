from random import randint
import math
def Descifrar(codificado,columnas):
    claro=''
    renglones=int(math.ceil(len(codificado)/float(columnas)))
    papel = [['' for x in range(renglones)] for y in range(columnas)]
    codificado=codificado + '*' * (renglones*columnas - len(codificado))
    k=0
    for i in range(columnas):
        for j in range(renglones):
            papel[i][j]=codificado[k]
            k+=1
    for i in range(renglones):
        for j in range(columnas):
            claro=claro + papel[j][i]
    return claro
C = [c.strip() for c in list(open('MerkleTC.txt','r'))]
N = len(C)

n = randint(0,N-1)
print('Se recibieron %d mensajes' % N)
print('Descifrando por FB, el numero %d:' % n)
print(C[0])
z=0; D=''
while D.find('MENSAJE')==-1:
    z+=1; k = randint(2,20)
    D = Descifrar(C[n],k)
    D = D.replace('*','')
print('El mensaje es:', D)
print('Se realizaron %d iteraciones.' % z)
