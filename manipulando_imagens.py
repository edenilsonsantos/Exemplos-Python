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
