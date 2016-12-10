from PIL import Image

# Carregando a imagem
im = Image.open("ceu.jpg")

# Buscando o tamanho da imagem
w,h = im.size
img1 = input("Porcentagem Imagem 1 ")
img2 = input("Porcentagem Imagem 2 ")
p1 = float(img1/100.0)
p2 = float(img2/100.0)
# Eximbindo a imagem (com o xv)
im.show()

spfc = Image.open("spfc.jpg")
blend = Image.new("RGB",(w,h))

for x in range(w):
 for y in range(h):
  r,g,b = im.getpixel((x,y))
  rs,gs,bs = spfc.getpixel((x,y))
  r = (int(r * p1) + int(rs * p2))
  g = (int(g * p1) + int(gs * p2))
  b = (int(b * p1) + int(bs * p2))
  blend.putpixel((x,y),(r,g,b))

blend.show()
