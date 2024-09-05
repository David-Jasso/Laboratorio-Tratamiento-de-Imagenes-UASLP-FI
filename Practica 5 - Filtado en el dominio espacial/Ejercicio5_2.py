import cv2 as cv
import numpy as np
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

def main():
    # Diccionario con todos los filtros a usar
    dict = {'Normal': 1,'Sobel': 2, 'Prewitt': 3, 'Roberts': 4, 'Canny': 5}
    # Filtro inicial
    filtro = dict['Normal']
    # Crear ventana
    win_name = 'Ejercicio 5.2'
    cv.namedWindow(win_name, cv.WINDOW_AUTOSIZE)

    vid_capture = cv.VideoCapture(0, cv.CAP_DSHOW)

    while True:
        ret, frame = vid_capture.read()

        if not ret:
            break

        if filtro == dict['Normal']:
            prep_frame = frame

        elif filtro == dict['Sobel']:
            prep_frame = cv.Sobel(frame, -1, 1, 1)
        
        elif filtro == dict['Prewitt']:
            # Operador de Prewitt
            prew_kernel_x = np.array([[-1, 0, 1],
                                      [-1, 0, 1],
                                      [-1, 0, 1]])
            
            prew_kernel_y = np.array([[-1, -1, -1],
                                      [0, 0, 0],
                                      [1, 1, 1]])
            
            # Aplicar filtros
            der_x = cv.filter2D(frame, cv.CV_64F, prew_kernel_x)
            der_y = cv.filter2D(frame, cv.CV_64F, prew_kernel_y)

            # Fusionar imagenes, convirtiendo a unit8
            absX = cv.convertScaleAbs(der_x)
            absY = cv.convertScaleAbs(der_y)

            prep_frame = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

        elif filtro == dict['Roberts']:
            rob_kernel_x = np.array([[1, 0],
                          [0, -1]])

            rob_kernel_y = np.array([[0, 1],
                          [-1, 0]])

            # Aplicar filtros
            der_x = cv.filter2D(frame, cv.CV_64F, rob_kernel_x)
            der_y = cv.filter2D(frame, cv.CV_64F, rob_kernel_y)

            # Fusionar images, convirtiendo a uint8
            absX = cv.convertScaleAbs(der_x)
            absY = cv.convertScaleAbs(der_y)

            prep_frame = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
        
        elif filtro == dict['Canny']:
            # Operador Canny
            prep_frame = cv.Canny(frame, 100, 200)
        
        cv.imshow(win_name, prep_frame)

        key = cv.waitKey(10)
        if key == ord('q'):
            break
        elif key == ord('s'):
            clear()
            filtro = dict['Sobel']
            print('Aplicando filtro de Sobel')
        elif key == ord('p'):
            clear()
            filtro = dict['Prewitt']
            print('Aplicando filtro de Prewitt')
        elif key == ord('r'):
            clear()
            filtro = dict['Roberts']
            print('Aplicando filtro de Roberts')
        elif key == ord('c'):
            clear()
            filtro = dict['Canny']
            print('Aplicando filtro de Canny')
        elif key == ord('n'):
            filtro = dict['Normal']
            clear()
            print('Mostrando camara sin filtros')
        
    vid_capture.release()
    cv.destroyAllWindows(win_name)

if __name__ == '__main__':
    main()

