#Exercicio2

#Exercicio4
#coding=utf-8
from PIL import Image

#Abre o arquivo da imagem
imcinza = Image.open("ceu.JPG")
#Obtem o tamanho de largura e altura
w,h = imcinza.size

immedia = Image.new("RGB",(w,h))
for x in range(w):
 for y in range(h):
  r,g,b = imcinza.getpixel((x,y))
  media = (r+g+b)/3
  immedia.putpixel((x,y),(media,media,media))

immedia.show()

im_max_min = Image.new("RGB",(w,h))
for x in range(w):
 for y in range(h):
  r,g,b = imcinza.getpixel((x,y))
  max_min = (max(r,g,b)+min(r,g,b))/2
  im_max_min.putpixel((x,y),(max_min,max_min,max_min))
im_max_min.show()

im_ponderada = Image.new("RGB",(w,h))
for x in range(w):
 for y in range(h):
  r,g,b = imcinza.getpixel((x,y))
  ponderada = int((r*0.299) + (g*0.587) + (b*0.114))
  im_ponderada.putpixel((x,y),(int(ponderada),int(ponderada),int(ponderada)))
im_ponderada.show()
