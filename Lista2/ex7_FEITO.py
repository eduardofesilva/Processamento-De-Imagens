from PIL import Image
import matplotlib.pyplot as plt
im = Image.open("ceu.jpg")

# Buscando o tamanho da imagem
w,h = im.size
valor = input("Valor")
imr=Image.new("RGB",(w,h))



for x in range(w):
 for y in range(h):
  # Busca os valores de RGB no pixel x,y
  r,g,b = im.getpixel((x,y))
  c = int((r*0.299) + (g*0.587) + (b*0.114))
  if(c<valor):
      imr.putpixel((x,y),(c,c,c))


imr.show()
