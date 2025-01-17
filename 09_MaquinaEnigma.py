def rota(Disco,n):
    if n<0: n = len(Disco)+n
    for i in range(n):
        B = [d for d in Disco]
        C = [Disco[d] for d in Disco]
        C.insert(0,C.pop(-1))
        Disco = {b:c for b,c in zip(B,C)}
    return Disco
CD = []

A = [n for n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

CD.append([n for n in 'FJDPMSQGWXEUYRATIVHNKZCLBO']) # Disco 0
CD.append([n for n in 'SIBTGVQEOYUMDKRFNPJLZCWHAX']) # Disco 1
CD.append([n for n in 'SGJYLTERXUKZWQHOVPDMFBNICA']) # Disco 2
CD.append([n for n in 'EFCVAKUSMBJPGZLHIONRYWDQXT']) # Disco 3
CD.append([n for n in 'RXDCLUSQPIGTHVFYOZJAKBMNEW']) # Disco 4
CD.append([n for n in 'NAUXHFRZISWGPLBDOQKMCTYVJE']) # Disco 5
CD.append([n for n in 'KJGVLSEBDZUCRHFXTWOYPMAQIN']) # Disco 6
CD.append([n for n in 'ZRFKEQPVSBTHOMXWULGINJDCYA']) # Disco 7

SelDiscos  = [2,6,3,0] # Seleccion del conjunto de discos
PosInicial = [4,1,6,1] # Seleccion de la posición inicial de los discos
Engranes   = [2,3,6,2] # Seleccion la rotacion de discos

D = [CD[i] for i in SelDiscos]

Discos  = [{a:d for a,d in zip(A,Di)} for Di in D]

for i,r in enumerate(PosInicial):
    Discos[i] = rota(Discos[i],r)

Texto = input('Mensaje: ')

Texto = Texto.replace(' ','')
Texto = Texto.upper()

En = ''

for L in list(Texto):
    for d in Discos: L = d[L]
    En = En + L
    for i,r in enumerate(Engranes):
        Discos[i] = rota(Discos[i],r)
        
print('Texto cifrado:',En)
