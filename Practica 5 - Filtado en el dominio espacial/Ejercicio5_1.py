import cv2 as cv
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

def main():
    # Diccionario con todos los filtros a usar
    dict = {'Normal': 1,'Caja': 2, 'Gauss': 3, 'Mediana': 4}
    # Filtro inicial
    filtro = dict['Normal']
    # Crear ventana
    win_name = 'Ejercicio 5.1'
    cv.namedWindow(win_name, cv.WINDOW_AUTOSIZE)

    vid_capture = cv.VideoCapture(0, cv.CAP_DSHOW)

    while True:
        ret, frame = vid_capture.read()

        if not ret:
            break

        if filtro == dict['Normal']:
            prep_frame = frame
        elif filtro == dict['Caja']:
            prep_frame = cv.blur(frame, (11, 11))
        elif filtro == dict['Gauss']:
            prep_frame = cv.GaussianBlur(frame, (11,11), 0)
        elif filtro == dict['Mediana']:
            prep_frame == cv.medianBlur(frame, 11)

        cv.imshow(win_name, prep_frame)

        key = cv.waitKey(10)
        if key == ord('q'):
            break
        elif key == ord('c'):
            filtro = dict['Caja']
            clear()
            print('Aplicando filtro de caja')
        elif key == ord('g'):
            clear()
            filtro = dict['Gauss']
            print('Aplicando filtro Gaussiano')
        elif key == ord('m'):
            clear()
            filtro = dict['Mediana']
            print('Aplicando filtro mediana')
        elif key == ord('n'):
            filtro = dict['Normal']
            clear()
            print('Mostrando camara sin filtros')
        
    vid_capture.release()
    cv.destroyAllWindows(win_name)

if __name__ == '__main__':
    main()

        