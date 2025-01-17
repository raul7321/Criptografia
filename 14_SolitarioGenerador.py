from random import randint
print('Generar configuracion inicial:')
opcion = input('1. de manera aleatoria 2. introducirla manualmente ')
def Swap(x,y):
    j,k = M[x],M[y]
    M[x],M[y] = k,j
archivo = open('LlaveSolitario.txt','w')
if opcion=='1':
    M = [i+1 for i in range(54)]
    for i in range(5000):
        a = randint(0,53)
        b = randint(0,53)
        Swap(a,b)
    print('El orden del mazo es:')
    
    for m in M:
        archivo.write(' %d\n' % m)
        print(m,end=' ')
else:
    for i in range(54):
        m = input('Carta '+str(i)+':')
        archivo.write(' %d\n' % m)
archivo.close()
