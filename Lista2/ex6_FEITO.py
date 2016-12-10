#Exercicio2

#Exercicio4
#coding=utf-8
from PIL import Image


imcinza = Image.open("spfc.jpg")
w,h = imcinza.size
n1 = [0 for i in range(256)]
z = 0

immedia = Image.new("RGB",(w,h))
for x in range(w):
 for y in range(h):
  r,g,b = imcinza.getpixel((x,y))
  z = (max(r,g,b)+min(r,g,b))/2
  #print z
  n1[z] = n1[z] + 1
#Cria 3 contadores Escuro(pixels com valor menor igual a 50)
# Indefinido qualquer valor entre 51 e 160
#Claro qualquer valor acima de 160
#Baseado no tamanho de cada contador e comparando os 3 defino sua classificacao
maior=total=escuro=indefinido=claro = 0
for x in range(len(n1)):
  if(n1[x]>maior):
    maior = n1[x]
  if(x<=50):
    escuro += n1[x]
  else:
    if(x<=160):
      indefinido += n1[x]
    else:
      claro += n1[x]

if (claro == max(claro,escuro,indefinido)):
  print "Imagem Clara"
if (escuro == max(claro,escuro,indefinido)):
  print "Imagem Escura"
if (indefinido == max(claro,escuro,indefinido)):
  print "Imagem Indefinida"
#print claro,escuro,indefinido
#immedia.show()
