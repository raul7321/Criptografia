from random import shuffle

def Pos(t,N):
    for r,n in enumerate(N):
        if t in n:
            return([r,n.index(t)])

def GeneraLLave():
    A = [chr(a) for a in range(65,91)] + [str(a) for a in range(2,8)]
    shuffle(A)
    return [[A.pop() for i in range(8)] for j in range(4)]

def Muestra(H):
    for m in M:
        for a in m:
            print(a,end = ' ')
        print()
    print()

def Acondiciona(T):
    R = [' ','.']
    for r in R: T = T.replace(r,'')
    p = ''; B = ''
    for t in T:
        p = p + t
        if len(p)==2:
            if p[0]!=p[1]:
                B = B + p 
            else:
                B = B + p[0]+'X'+p[1]
            p = ''
    B = B + p
    if len(B)%2: B = B + 'X'
    return B

def Separa(T):
    return [[T[i],T[i+1]] for i in range(0,len(T)-1,2)]

def Encripta(T):
    AC = Acondiciona(T)
    R = Separa(AC)
    TE = ''
    for par in R:
        [r1,c1] = Pos(par[0],M)
        [r2,c2] = Pos(par[1],M)
        if r1==r2:
            k1 = M[r1][(c1+1)%8]
            k2 = M[r1][(c2+1)%8]
        elif c1==c2:
            k1 = M[(r1+1)%4][c1]
            k2 = M[(r2+1)%4][c1]
        else:
            k1 = M[r1][c2]
            k2 = M[r2][c1]
        TE = TE + (k1+k2 + ' ')
    return TE

def desEncripta(T):
    AC = Acondiciona(T)
    R = Separa(AC)
    TE = ''
    for par in R:
        [r1,c1] = Pos(par[0],M)
        [r2,c2] = Pos(par[1],M)
        if r1==r2:
            k1 = M[r1][(c1-1)%8]
            k2 = M[r1][(c2-1)%8]
        elif c1==c2:
            k1 = M[(r1-1)%4][c1]
            k2 = M[(r2-1)%4][c1]
        else:
            k1 = M[r1][c2]
            k2 = M[r2][c1]
        TE = TE + (k1+k2 + ' ')
    return TE

TC = input('Mensaje: ').upper()

print()

M = GeneraLLave()
Muestra(M)

TE = Encripta(TC)
print('Cifrado:   ',TE)

TC = desEncripta(TE)

print('Descifrado:',TC)
