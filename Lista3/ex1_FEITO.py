from PIL import Image

# Carregando a imagem
im = Image.open("ceu.JPG")
# Buscando o tamanho da imagem
w,h = im.size

# Eximbindo a imagem (com o xv)
im.show()

# Dica: trabalhe a imagem original em uma nova imagem
# criando uma nova imagem "RGB" do mesmo tamanho da
# original
imluz=Image.new("RGB",(w,h))


# Exercicio 1: adicionar luminosidade a imagem

# Para cada Linha e coluna
for x in range(w):
 for y in range(h):
  # Busca os valores de RGB no pixel x,y
  r,g,b = im.getpixel((x,y))

  # Adiciona 100 (tendendo ao branco), com limite em 255
  if r + 100 < 255:
    r = r + 100
  else:
    r = 255

  if g + 100 < 255:
    g = g + 100
  else:
    g = 255

  if b + 100 < 255:
    b = b + 100
  else:
    b = 255

  # Grava o pixel na nova imagem
  imluz.putpixel((x,y),(r,g,b))

# Exibe a nova imagem
imluz.show()
