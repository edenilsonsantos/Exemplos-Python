# pip install opencv-python
import cv2

#######################################################
# Converter imagem para escala de cinza
filename_color = r'c:\temp\imagem_teste.png'
img = cv2.imread(filename_color, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'c:\temp\imagem_cinza.png',img)


#######################################################
# Recortar imagem 
filename_gray = r'c:\temp\imagem_cinza.png'
img = cv2.imread(filename_gray)
altura, largura, borda = img.shape
img_recort = img[0:altura - 100, 0:largura - 100, 0:borda]

# img_recort = img[altura_ini:alt_fim, largura_ini:larg_fim, borda]
# img_recort = img[0:243, 0:500, 0:3]

cv2.imwrite(r'c:\temp\imagem_recortada.png', img_recort)

#######################################################
# novo
filename_color = r'c:\temp\imagem_teste.png'
img = cv2.imread(filename_color, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'c:\temp\imagem_cinza.png',img)
