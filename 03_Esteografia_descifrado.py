from PIL import Image

def suma(a,b):
    return list(map(sum,zip(a,b)))

referencia='ABCDEFGHIJKLMNOPQRSTUVWXYZ*'

archivo='perro1.png'
img = Image.open(archivo)
pixeles=img.load()

(k,x,y)=(0,100,100)
(r,g,b)=(0,0,0)
simple = ''
while referencia[r+g+b] !='*':
    p=(0,0,0)
    for i in range(-1,2):
        for j in range(-1,2):
            if (i,j)!=(0,0):
                p=suma(p,pixeles[x+i+2*k, y+j])
    r = abs(pixeles[x+2*k,y][0]-int(p[0]/8))
    g = abs(pixeles[x+2*k,y][1]-int(p[1]/8))
    b = abs(pixeles[x+2*k,y][2]-int(p[2]/8))
    k=k+1
    simple=simple + referencia[r+g+b]

print(simple)

