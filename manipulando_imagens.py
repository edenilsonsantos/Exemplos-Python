# pip install opencv-python
# pip install pytesseract
# https://yangcha.github.io/iview/iview.html
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Edenilson\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#######################################################
# LER, IMPRIMIR IMAGEM NA TELA, E CAPTURAR AS DIMENSÕES
# Cada pixel da imagem contém um % de 3 cores, vermelho, verde e azul (RGB), cada cor pode ter o valor de 0 a 255.
# pixel = [200, 12, 53],   print(img.shape)

img_path = r'c:\temp\tela_mua1.png'
img = cv2.imread(img_path)
altura_img, largura_img, qtd_canais_cores = img.shape
print(altura_img, largura_img, qtd_canais_cores)
cv2.imshow('minha imagem', img)
cv2.waitKey(0)


#######################################################
# CONVERTER IMAGEM PARA ESCALA CINZA
filename_color = r'c:\temp\imagem_teste.png'
img = cv2.imread(filename_color, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'c:\temp\imagem_cinza.png',img)


#######################################################
# RECORTAR IMAGEM 
filename_gray = r'c:\temp\imagem_cinza.png'
img = cv2.imread(filename_gray)
altura, largura, qtd_canais_de_cores = img.shape
img_recort = img[0:altura - 100, 0:largura - 100, 0:borda]

# img_recort = img[altura_ini:alt_fim, largura_ini:larg_fim, qtd_canais_de_cores]
# img_recort = img[0:243, 0:500, 0:3]

cv2.imwrite(r'c:\temp\imagem_recortada.png', img_recort)

#######################################################
# ALTERANDO VALOR DE PIXEL DA IMAGEM
# alterar uma posicao de pixel para preto
# img[0][0] = [0, 0, 0]
# alterar uma posicao de pixel para branco
# img[0][0] = [255, 255, 255]

img_path = r'c:\temp\tela_mua1.png'
img = cv2.imread(img_path)
img[0:100, 0:8] = (255, 255, 255)
cv2.imshow('minha imagem', img)
cv2.waitKey(0)

#######################################################
# MANIPULAR AS CORES DE PIXEL ITERANDO A IMAGEM TODA
img_path = r'c:\temp\tela_mua1.png'
im = Image.open(img_path)
img = cv2.imread(img_path)
img1 = cv2.imread(img_path)
img2 = cv2.imread(img_path)
img3 = cv2.imread(img_path)
img4 = cv2.imread(img_path)
img5 = cv2.imread(img_path)
branco = (255, 255, 255)

#Exemplos:
# trocando todos os pixes pela cor branco
for i in range(0, img1.shape[0]):
    for j in range(0, img1.shape[1]):
        img1[i, j] = branco
cv2.imshow('minha imagem', img1)
cv2.waitKey(0)

# add 1 pixel branco saltando a posicao de 10 em 10 para altura e largura (linha, coluna)        
for i in range(0, img2.shape[0], 10):
    for j in range(0, img2.shape[1], 10):
        img2[i, j] = branco
cv2.imshow('minha imagem', img2)
cv2.waitKey(0)
  
# add 1 pixel branco saltando a posicao de 10 em 10 apenas para altura (linha)                 
for i in range(0, img3.shape[0], 10):
    for j in range(0, img3.shape[1]):
        img3[i, j] = branco
cv2.imshow('minha imagem', img3)
cv2.waitKey(0)

# pintar intervalos de pixels, exemplo de i ate i+5, de j até j+5
for i in range(0, img4.shape[0], 10):
    for j in range(0, img4.shape[1], 10):
        img4[i:i+5, j:j+5] = branco
cv2.imshow('minha imagem', img4)
cv2.waitKey(0)

# Obter os 3 valores rgb do pixel, pelo link abaixo.
# https://yangcha.github.io/iview/iview.html
# no loop usando matriz tridimensional da img, a terceira posicao é o rgb
# lembrando que temos entao: img[altura, largura, canal_rgb]
# Indice de leitura do RGB
R = 2
G = 1
B = 0
# abaixo codigo da cor do pixel que desejo substituir a cor, por branco
# R, G, B)
(213, 225, 236)
# outro
(233, 241, 248)

# alteração sem iterar com for
img5[0:100, 0:8] = (255, 255, 255)
img5[0:100, 60:100] = (255, 255, 255)
img5[0:15, 0:100] = (255, 255, 255)

# alteração iterando com for
for i in range(0, img5.shape[0]):
    for j in range(0, img5.shape[1]):
        # print(img5[i, j, B])
        # Se eu encontrar a cor que desejo, substituir a cor do pixel por branco.
        if (img5[i, j, R] == 213) and (img5[i, j, G] == 225) and (img5[i, j, B] == 236):
            img5[i, j] = branco
        if (img5[i, j, R] == 233) and (img5[i, j, G] == 241) and (img5[i, j, B] == 248):
            img5[i, j] = branco
cv2.imshow('minha imagem', img5)
cv2.waitKey(0)



################################################################
# OCR - DEPOIS DE IMAGEM TRATADA e ZOOM

import cv2
import numpy as np
import pytesseract

# # https://yangcha.github.io/iview/iview.html
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Edenilson\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#dilation, remove characters
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

# aplicar zoom 
def zoom(img, zoom_factor=1.5):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor) 

### Tratar imagem
filename = r'c:\temp\tela_mua1.png'
img = cv2.imread(filename)
img2 = cv2.imread(filename)
branco = (255, 255, 255)
img[0:100, 0:8] = (255, 255, 255)
img[0:100, 60:100] = (255, 255, 255)
img[0:15, 0:100] = (255, 255, 255)
R, G, B = 2,1,0

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if (img[i, j, R] == 213) and (img[i, j, G] == 225) and (img[i, j, B] == 236):
            img[i, j] = branco
        if (img[i, j, R] == 233) and (img[i, j, G] == 241) and (img[i, j, B] == 248):
            img[i, j] = branco
            

img = zoom(img, 2.5)
cv2.imshow('minha imagem', img)
cv2.waitKey(0)
# filename = r'c:\temp\imagem_pronta.png'
# cv2.imwrite(filename, img)
# time.sleep(2)



# OCR - Extração de numeros de conta
# Adding custom options
custom_config = r'--psm 12 --oem 3 -c tessedit_char_whitelist=0-123456789'
contas = pytesseract.image_to_string(img, config=custom_config)
print(contas)
list_contas = contas.split()
print(list_contas)
