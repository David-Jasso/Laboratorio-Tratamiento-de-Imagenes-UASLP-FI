import cv2 as cv
import numpy as np

img = cv.imread('Recursos/Hollow Knight.jpg')
img = cv.resize(img, None, fx = 0.5, fy=0.5)

# Conseguir los parametros de ancho y alto de la imagen
alto, ancho = img.shape[:2]

# Conseguir los valores de tx y tx para la traslacion
tx, ty = ancho/4, alto/4

# crear matriz de traslacion, se crea un arreglo de NumPy
tras_matriz = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

img = cv.warpAffine(img, tras_matriz, (ancho, alto))

#Rotacion de imagen
centro = (ancho/2, alto/2)
rot_matriz = cv.getRotationMatrix2D(centro, 45, 1.0)
img = cv.warpAffine(img, rot_matriz, (ancho, alto))


cv.imshow('Ventana 4.1', img)
cv.waitKey(0)
cv.destroyAllWindows()