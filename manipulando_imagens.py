# pip install opencv-python
import cv2

#######################################################
# Lendo e Imprimindo uma imagen na tela
# Cada pixel da imagem contém um % de 3 cores, vermelho, verde e azul (RGB), cada cor pode ter o valor de 0 a 255.
# pixel = [200, 12, 53],   print(img.shape)

img_path = r'c:\temp\tela_mua1.png'
img = cv2.imread(img_path)
altura_img, largura_img, qtd_canais_cores = img.shape
print(altura_img, largura_img, qtd_canais_cores)
cv2.imshow('minha imagem', img)
cv2.waitKey(0)


#######################################################
# Converter imagem para escala de cinza
filename_color = r'c:\temp\imagem_teste.png'
img = cv2.imread(filename_color, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'c:\temp\imagem_cinza.png',img)


#######################################################
# Recortar imagem 
filename_gray = r'c:\temp\imagem_cinza.png'
img = cv2.imread(filename_gray)
altura, largura, qtd_canais_de_cores = img.shape
img_recort = img[0:altura - 100, 0:largura - 100, 0:borda]

# img_recort = img[altura_ini:alt_fim, largura_ini:larg_fim, qtd_canais_de_cores]
# img_recort = img[0:243, 0:500, 0:3]

cv2.imwrite(r'c:\temp\imagem_recortada.png', img_recort)

#######################################################
# novo
filename_color = r'c:\temp\imagem_teste.png'
img = cv2.imread(filename_color, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'c:\temp\imagem_cinza.png',img)
