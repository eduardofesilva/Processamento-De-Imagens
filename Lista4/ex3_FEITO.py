#Exercicio2

#Exercicio4
#coding=utf-8
from PIL import Image


im1 = Image.open("facens.jpg")
im2 = Image.open("fundo2.png")
w,h = im1.size

imagem_nova = Image.new("RGB",(w,h))
for x in range(w):
 for y in range(h):
  r,g,b = im1.getpixel((x,y))
  r1,g1,b1,a = im2.getpixel((x,y))
  if a==0:
      imagem_nova.putpixel((x,y),(r,g,b))
  else:
      imagem_nova.putpixel((x,y),(r1,g1,b1))
  #imagem_nova.putpixel((x,y),(r+r1,g+g1,b+b1,a))

imagem_nova.show()
