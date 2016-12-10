#Exercicio 1 - Lista 1


from PIL import Image


imcinza = Image.open("ceu.JPG")#imagem base
w,h = imcinza.size
#Canal Vermelho
im_r = Image.new("RGB",(w,h))#copia canal vermelho
for x in range(w):
 for y in range(h):
  r,g,b = imcinza.getpixel((x,y))#obtem R,G,B de cada ponto x,y da imagem
  im_r.putpixel((x,y),(r,r,r))
#Canal Verde
im_g = Image.new("RGB",(w,h))
for x in range(w):
    for y in range(h):
        r,g,b = imcinza.getpixel((x,y))#obtem R,G,B de cada ponto x,y da imagem
        im_g.putpixel((x,y),(g,g,g))
#Canal Azul
im_b = Image.new("RGB",(w,h))
for x in range(w):
    for y in range(h):
        r,g,b = imcinza.getpixel((x,y))#obtem R,G,B de cada ponto x,y da imagem
        im_b.putpixel((x,y),(b,b,b))


im_r.show()
im_g.show()
im_b.show()
