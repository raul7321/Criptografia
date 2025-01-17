from random import randint
def ordN(c):
    if c.isdigit(): return ord(c)+43
    return ord(c)
def chrN(i):
    if i>90: return chr(i-43)
    return chr(i)
def Cifra(C,K):
    return ''.join([chrN(65+(ordN(m)-65+K[i%len(K)])%36) for i,m in enumerate(C)])
def Descifra(E,K):
    return ''.join([chrN(65+(ordN(m)-65-K[i%len(K)])%36) for i,m in enumerate(E)])

Dicc = ['Hola','perro','casa','Mensaje','Guerra','termino']

M = 'ESTEESUNMENSAJEHISTORICO'
Lk = 7
KC = [randint(0,9) for i in range(Lk)]
Z = Cifra(M,KC)

cT=0
for L in range(2,10):
    for k in range(10**L):
        K = [int(m) for m in ('0'*(L-len(str(k)))+str(k))] #Genera Llave
        D = Descifra(Z,K)
        logrado = False
        for m in Dicc:
            cT+=1
            if D.find(m.upper())!=-1: logrado=True
        if logrado: break
    if logrado:
        print ('Cifrado:',Z)
        print ('Descifrado por FB:',D)
        print ('Llave encontrada:',K)
        print ('Operaciones: ',cT)
        break
    else:
        print ('Fallo el ataque por FB para llave de %d digitos' % L)
