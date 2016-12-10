#Exercicio2

#Exercicio4
#coding=utf-8
from PIL import Image
im = Image.open("ceu.JPG")
im.show()
# Buscando o tamanho da imagem
w,h = im.size
imneg = Image.new("RGB",(w,h))

for x in range(w):
 for y in range(h):
  r,g,b = im.getpixel((x,y))
  r = 255 - r
  g = 255 - g
  b = 255 - b
  imneg.putpixel((x,y),(r,g,b))

imneg.show()
