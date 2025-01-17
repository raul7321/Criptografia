def hash01(Cadena):
    p=0; s=0; M=50000
    for i,m in enumerate(Cadena):
        p=p+ord(m)
        z=256**i
        s=s+z*ord(m)
    St=str(s %M)
    St=(len(str(M))-len(St))*str(p %10)+St
    return St 

Mensaje=input('Dame la cadena de entrada: ')
print('La salida de la funcion Hash1 es:', hash01(Mensaje))
