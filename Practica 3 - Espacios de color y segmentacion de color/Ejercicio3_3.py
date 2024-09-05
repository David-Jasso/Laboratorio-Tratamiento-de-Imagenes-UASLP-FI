import cv2 as cv
import numpy as np
import os

tol = 7
showing = False

#Función Callback para hacer la segmentación de color
#en base al color de la imagen que se le hace click.
def mouseFunc(evento, x, y, flags, imag):
    global showing
    #Si hacemos click izquierdo
    if evento == cv.EVENT_LBUTTONDOWN:
        #Cambiamos la imagen de espacio de color BGR a HSV.
        hsv = cv.cvtColor(imag, cv.COLOR_BGR2HSV)
        os.system('cls')
        #Obtención e impresión de los canales del espacio de color HSV.
        mat, sat, val = hsv[y,x]
        print(f'[{mat},{sat},{val}]')
        #Segmentación de color
        if (mat - tol ) >= 0 and (mat + tol) <= 255:
            lower = np.array((mat - tol, 10, 50), np.uint8)
            upper = np.array((mat + tol, 255, 255), np.uint8)
            mascara = cv.inRange(hsv, lower, upper)
        else:
            lower = np.array((0, 10, 50), np.uint8)
            upper = np.array((0 + tol, 255, 255), np.uint8)
            bin_img = cv.inRange(hsv, lower, upper)

            lower = np.array((255 - tol, 10, 50), np.uint8)
            upper = np.array((255 + tol, 255, 255), np.uint8)
            bin2_img = cv.inRange(hsv, lower, upper)

            mascara = cv.bitwise_or(bin_img, bin2_img)

        res = cv.bitwise_and(imag, imag, mask = mascara)
        cv.imshow('Segmentacion', res)
        showing = True

#Definición de la función principal
def main():
    img = cv.imread('Imagenes/Stardew Valley.jpg')
    img = cv.resize(img, None, fx=0.5, fy=0.5)
    cv.namedWindow('Colores')
    cv.setMouseCallback('Colores', mouseFunc, img)

    while True:
        cv.imshow('Colores', img)
        key = cv.waitKey(1)
        if key == ord('q'):
            break

    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
