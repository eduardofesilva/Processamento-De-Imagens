from PIL import Image

# Carregando a imagem
im = Image.open("ceu.jpg")
w,h = im.size

im.show()

spfc = Image.open("spfc.jpg")
blend = Image.new("RGB",(w,h))
imagem = 1 # funciona como um chaveador entre as 2 imagens
for x in range(w):
 for y in range(h):
  r,g,b = im.getpixel((x,y))
  rs,gs,bs = spfc.getpixel((x,y))
  if imagem ==1:
      blend.putpixel((x,y),(r,g,b))
  if imagem ==-1:
      blend.putpixel((x,y),(rs,gs,bs))
  imagem=imagem*-1

blend.show()
