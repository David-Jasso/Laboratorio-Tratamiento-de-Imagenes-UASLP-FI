import cv2 as cv
import numpy as np

def main():
    # Cargar la imagen de monedas
    img = cv.imread('Laboratorio TI/Practica 6 - Deteccion de contornos/Imagenes/Monedas.png')
    # Convertir la imagen a escala de grises
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Aplicar un filtro gaussiano
    gray = cv.GaussianBlur(gray, (5, 5), 3)

    # Aplicar umbralizado
    _, thresh = cv.threshold(gray, 1, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    # Aplicar deteccion de bordes Canny
    canny = cv.Canny(thresh, 150, 255)

    # Encontrar contornos
    contours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print(f'Se han encontrado: {len(contours)} monedas en la imagen')
    cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    for cnt in contours:
        mo = cv.moments(cnt)
        if mo['m00'] != 0:
            cx = mo['m10'] / mo['m00']
            cy = mo['m01'] / mo['m00']
        area = mo['m00']
        cv.putText(thresh, str(area), (np.int0(cx)-20, np.int0(cy)), cv.FONT_HERSHEY_COMPLEX, fontScale=0.45, color=(0,0,0), thickness=1)
        cv.drawMarker(img, (np.int0(cx), np.int0(cy)), (0, 255, 0), cv.MARKER_CROSS)
    
    cv.imshow('Contornos', img)
    cv.imshow('Areas', thresh)
    cv.waitKey(0)

if __name__ == '__main__':
    main()