import cv2 as cv
import numpy as np

#Cargar la imagen y reducir tamaño
img = cv.imread('Recursos/Hollow Knight.jpg')
img = cv.resize(img, None, fx = 0.5, fy = 0.5)
img = np.float32(img/255)

window = 'Ejercicio 4.3'

#Asignación de valores para el contraste y el brillo
contrast = 10
max_contrast = 100
brightness = 0
max_brightness = 100


#Funciones para aumentar el brillo y contraste
# usando la funcion g(i,j)=α⋅f(i,j)+β 
def change_contrast(val):
    global contrast
    contrast = val/10
    perform_operation()

def change_brightness(val):
    global brightness
    brightness = val/100
    perform_operation()

def perform_operation():
    im1 = img*contrast + brightness
    cv.imshow(window, im1)


#Impresión de la ventana y creación de trackbar para aumentar el brillo y contraste
cv.imshow(window, img)
cv.createTrackbar("Contrast", window, contrast, max_contrast, change_contrast)
cv.createTrackbar("brightness", window, brightness, max_brightness, change_brightness)

#Cerrar ventana
while True:
    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()