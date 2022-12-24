# pip install opencv-python
import cv2

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
