#Exercicio 5
# Cada f.read() le um tamanho especifico do arquivo
#https://docs.python.org/2/tutorial/inputoutput.html
# Cada struct unpack le uma estrutura C e converte para um valor string contendo
#um unico item. O struckt unpack realiza tambem o processo de offset
#https://docs.python.org/2/library/struct.html
#Leitura do Header baseado nesse link https://en.wikipedia.org/wiki/BMP_file_format

import struct, sys, os
f = open('ex5.bmp')
b = f.read(2) # Bitmap format
if not b in ["BM", "BA", "CI", "CP", "IC", "PT"]:
    raise BitmapException("Não é um formato de bitmap file valido")

b = f.read(4) # Tamanho do Arquivo
size = struct.unpack("<i", b)[0]

b = f.read(4) #Lixo

b = f.read(4) # Comeca o offset efetivo para captura das informacoes da imagem
img_off = struct.unpack("<i", b)[0]

b = f.read(4) # Tamanho do Header
hdr_len = struct.unpack("<i", b)[0]
if hdr_len == 40:
    header = "BITMAPINFOHEADER"

    b = f.read(4) # Largura
    width = abs(struct.unpack("<i", b)[0])
    b = f.read(4) # Altura
    height = abs(struct.unpack("<i", b)[0])

    b = f.read(2) # Plano de Cores
    planes = struct.unpack("<i", b + "\x00\x00")[0]

    b = f.read(2) # Bits por pixel
    bpp = struct.unpack("<i", b + "\x00\x00")[0]

    b = f.read(4) # Tipo de compressão
    try:
        compression = self.compressiontypes[struct.unpack("<i", b)[0]]
    except:
        compression = "Desconhecido"

    b = f.read(4) # Resolucão Horizontal
    hres = struct.unpack("<i", b)[0]
    b = f.read(4) # Resolucão Vertical
    vres = struct.unpack("<i", b)[0]

    b = f.read(4) # Numero da Paleta de Cores
    colorcount = struct.unpack("<i", b)[0]

    b = f.read(4) # Cores Importantes ?????? Até agora nao entendi essa info
    impcolors = struct.unpack("<i", b)[0]
#print size,img_off,hdr_len
print "Cabecalho, Largura, Altura, Planes, Bits por pixel, Compressao, Resolucao Horizontal, Resolucao Verticial"
print header,width,height,planes,bpp,compression,hres,vres,colorcount
