# Biblioteca de imagens
from PIL import Image
import matplotlib.pyplot as plt
im = Image.open("ceu.jpg")

# Buscando o tamanho da imagem
w,h = im.size
#Cria uma copia para cada canal
imr=Image.new("RGB",(w,h))
img=Image.new("RGB",(w,h))
imb=Image.new("RGB",(w,h))
imc=Image.new("RGB",(w,h))
imm=Image.new("RGB",(w,h))
imy=Image.new("RGB",(w,h))
for x in range(w):
 for y in range(h):
  # Busca os valores de RGB no pixel x,y
  r,g,b = im.getpixel((x,y))
  imr.putpixel((x,y),(r,r,r))
  img.putpixel((x,y),(g,g,g))
  imb.putpixel((x,y),(b,b,b))
  imc.putpixel((x,y),((1-(r/255)),g,b))#C
  imm.putpixel((x,y),(r,(1-(g/255)),b))#M
  imy.putpixel((x,y),(r,g,(1-(b/255))))#Y

im.show()
imr.show()
img.show()
imb.show()
imc.show()
imm.show()
imy.show()
