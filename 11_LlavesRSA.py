from random import randrange

def mcd(a,b):
    return a if b==0 else mcd(b,a %b)

def primorelativo(p):
    q = 0
    while mcd(p,q)!=1:
        q = randrange(100,5000)
    return q

def primo():
    n = randrange(30)
    p = 2*n**2+39
    return p

def cp(r,e):
    d = 1
    while (e*d) %r!=1:
        d = randrange(r-1)
    return d

p = primo()
q = primo()
while p==q: q = primo()
n = p*q
rho = (p-1)*(q-1)
e = primorelativo(rho)
d = cp(rho,e)
print('p =', p)
print('q =', q)
print('n =', n)
print('rho =',rho)
print('e =', e)
print('d =',d)
print('Llave publica (%d, %d)' % (n,e))
print('Llave privada (%d, %d)' % (d,n))
