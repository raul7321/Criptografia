from PIL import Image

def suma(a,b):
    return list(map(sum,zip(a,b)))
def codifica(n):
    if n>=18:
        return (9,9,n%9)
    elif n>9:
        return(9,n%9,0)
    else:
        return(n,0,0)

mensaje = input('Mensaje a ocultar: ').upper().replace(' ','')

referencia = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*'

archivo = 'perro.png'
img = Image.open(archivo)
pixeles = img.load()

x = y = 100

mensaje=mensaje+'*'
for letra in range(len(mensaje)):
    p = [0,0,0]
    codigo=referencia.find(mensaje[letra])
    for i in range(-1,2):
        for j in range(-1,2):
            if (i,j)!=(0,0):
                p = suma(p,pixeles[x+i+2*letra, y+j])
    if int(p[0]/8)>=127:
        r = int(p[0]/8)-codifica(codigo)[0]
    else:
        r = int(p[0]/8)+codifica(codigo)[0]
    if int(p[1]/8)>=127:
        g = int(p[1]/8)-codifica(codigo)[1]
    else:
        g = int(p[1]/8)+codifica(codigo)[1]
    if int(p[0]/8)>=127:
        b = int(p[2]/8)-codifica(codigo)[2]
    else:
        b = int(p[2]/8)+codifica(codigo)[2]
            
    pixeles[x+2*letra,y]=(r,g,b)

img.save('perro1.png')
print('Mensaje -',mensaje, '- incluido en imagen')
img.show()
