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

    # Dibujar contornos
    cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    # Calcular cantidad de monedas
    cantidad_total = 0.0
    conteo = 0

    for cnt in contours:
        mo = cv.moments(cnt)
        if mo['m00'] != 0:
            cx = mo['m10'] / mo['m00']
            cy = mo['m01'] / mo['m00']
        area = mo['m00']
        cv.putText(thresh, str(area), (np.int0(cx)-20, np.int0(cy)), cv.FONT_HERSHEY_COMPLEX, fontScale=0.45, color=(0,0,0), thickness=1)
        cv.drawMarker(img, (np.int0(cx), np.int0(cy)), (0, 255, 0), cv.MARKER_CROSS)
        for peso in pesos:
            if abs(area- pesos[peso]['area']) <= tolerancia:
                valor = pesos[peso]['valor']
                pesos[peso]['cuenta'] += 1
                cantidad_total += pesos[peso]['valor']
                cv.putText(thresh, str(area), (np.int0(cx)-20, np.int0(cy)), cv.FONT_HERSHEY_COMPLEX, fontScale=0.45, color=(0,0,0), thickness=1)
                conteo += 1
    
    for peso in pesos:
        valor = pesos[peso]['valor']
        cuenta = pesos[peso]['cuenta']
        print(f'Monedas de ${valor}: {cuenta}')
    print("________________________")
    cantidad_total = round(cantidad_total, 3)
    print(f'Total: ${cantidad_total}')
    print(f'Cantidad de monedas: {conteo}')
    cv.imshow('Original', img)
    cv.imshow('Umbralizada', thresh)
    cv.waitKey(0)
    cv.destroyAllWindows()

global pesos, tolerancia
tolerancia = 20
pesos = {
    "20 Peso": {
        "valor": 20.0,
        "area": 11080,
        "cuenta": 0.0,
    },
    "10 Peso": {
        "valor": 10.0,
        "area": 10230,
        "cuenta": 0.0,
    },
    "5 Peso": {
        "valor": 5.0,
        "area": 9970,
        "cuenta": 0.0,
    },
    "2 Peso": {
        "valor": 2.0,
        "area": 8510,
        "cuenta": 0.0,
    },
    "1 Peso": {
        "valor": 1.0,
        "area": 7370,
        "cuenta": 0.0,
    },
    "0.5 Peso": {
        "valor": 0.5,
        "area": 7550,
        "cuenta": 0.0,
    }, 
    "0.2 Peso": {
        "valor": 0.2,
        "area": 6700,
        "cuenta": 0.0,
    },
    "0.1 Peso": {
        "valor": 0.1,
        "area": 5325,
        "cuenta": 0.0,
    }, 
    "0.05 Peso": {
        "valor": 0.05,
        "area": 4160,
        "cuenta": 0.0,
    }, 
}

if __name__ == '__main__':
    main()