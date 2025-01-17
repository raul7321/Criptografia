cripto = input('Dame las cifras del mensaje separadas por comas: ')
tabla = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = map(int,cripto.split(','))
print('Dame la llave privada (d,n)')
d = int(input('d = '))
n = int(input('n = '))
A = [b**d %n for b in B]
As = ''.join(map(str,A))
An = [int(As[k:k+2]) for k in range(0,len(As),2)]
for i,k in enumerate(A):
    print('a'+str(i) + ' = ' + str(k))
des = ''.join([tabla[i-11] for i in An])
print('Mensaje desencriptado:', des)
