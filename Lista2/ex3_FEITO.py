#Exercicio4
#coding=utf-8
from PIL import Image


imcinza = Image.open("ceu.JPG")

w,h = imcinza.size

imlimi = Image.new("RGB",(w,h))
valor = input("Valor limite ")

for x in range(w):
 for y in range(h):
  r,g,b = imcinza.getpixel((x,y))
  if (r > valor) or (g > valor) or (b > valor):
   r = 255
   g = 255
   b = 255
  else:
   r = 0
   g = 0
   b = 0
  imlimi.putpixel((x,y),(r,r,r))

imlimi.show()
