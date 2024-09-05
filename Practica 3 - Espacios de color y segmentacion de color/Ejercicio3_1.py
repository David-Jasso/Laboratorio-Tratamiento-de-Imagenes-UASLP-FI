import cv2 as cv
import numpy as np

img = cv.imread('Imagenes/Stardew Valley.jpg')
#Conversion de espacio de color BGR a HSV
img2 = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mostrar = True

while mostrar:
    cv.imshow('Espacio BGR', img)
    cv.imshow('Espacio HSV', img2)

    key = cv.waitKey(1)
    if key == ord('q'):
        mostrar = False

cv.destroyAllWindows('Espacio BGR')
cv.destroyAllWindows('Espacio HSV')
