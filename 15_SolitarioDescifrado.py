def Swap(x,y):
    j,k = M[x],M[y]
    M[x],M[y] = k,j
# Las cartas son los numeros del 1 al 54
# el indice del arreglo que modela al mazo va del 0 al 53
tabla = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
opcion=input('Quieres: 1. Encriptar, 2. Descifrar')
Texto=input('Texto: ')
Texto = Texto.replace(' ','') # Se eliminan los espacios
Texto = Texto.upper() # Se pasa a mayusculas
Codificado = []
for m in Texto:
    Codificado = Codificado + [tabla.find(m)+1]
L = list(open('LlaveSolitario.txt','r'))
M=[]
for l in L:
    l = l.replace('\n','')
    M=M+[int(l)]
ComodinA = 53
ComodinB = 54
Salida=[]
while len(Salida)<len(Texto):
    Comodin1 = M.index(ComodinA) # Posicion del comodin 1
    Swap(Comodin1,(Comodin1+1) %54)
    Comodin2 = M.index(ComodinB) # Posicion del comodin 2
    Swap(Comodin2,(Comodin2+1) %54)
    if M[53]==ComodinB:
        M = [M[0]]+[M[53]]+M[1:53]
    else:
        Swap((Comodin2+1) %54,(Comodin2+2) %54)
    Comodin1=min(M.index(ComodinA),M.index(ComodinB))
    Comodin2=max(M.index(ComodinA),M.index(ComodinB))
    M = M[Comodin2+1:54]+[M[Comodin1]]+M[Comodin1+1:Comodin2]+[M[Comodin2]]+M[0:Comodin1]
    Ultima = M[53]
    M = M[Ultima:53]+ M[0:Ultima]+[Ultima]
    Primera = M[0]
    if Primera==54: Primera=53
    if M[Primera]!=ComodinA and M[Primera]!=ComodinB:
        Salida = Salida+[M[Primera]]
k = ''
for i,m in enumerate(Codificado):
    k = k+tabla[(m+Salida[i]-1) %26]
if opcion=='1':
    print('Cifrado:',k)
else:
    claro = ''
    for i,n in enumerate(Codificado):
        p=(n-Salida[i]-1) %26
        claro = claro + tabla[p]
    print('Descifrado:',claro)
