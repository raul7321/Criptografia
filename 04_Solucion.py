from random import choice
import time
a1  = 'SEND'
a2  = 'MORE'
a3 = 'MONEY'
a0 = list(set(a1)|set(a2)|set(a3)) #Union de Conjuntos
D = {} # Diccionario vacio

A1 = A2 = A3 = 1; Cont = 0
ahora = time.time()
while A1+A2!=A3:
    B1 = list(range(10))
    B2 = list(range(1,10))
    for i in a0:
        D[i]= choice(B2) if (i=='M' or i=='S') else choice(B1)
        if D[i] in B1: B1.remove(D[i])
        if D[i] in B2: B2.remove(D[i])                      
    A1=sum([(10**(len(a1)-i-1))*D[k] for i,k in enumerate(a1)])
    A2=sum([(10**(len(a2)-i-1))*D[k] for i,k in enumerate(a2)])
    A3=sum([(10**(len(a3)-i-1))*D[k] for i,k in enumerate(a3)])
    Cont+=1
tiempo = time.time()-ahora
print('%d operaciones, en %.2f segundos.' % (Cont,tiempo))
print('%d operaciones por segundo.' % (Cont/tiempo))

for d in D: print ('%s = %d' % (d,D[d]))
print()
print('  %d\n+ %d\n-------\n %d' % (A1,A2,A3))
