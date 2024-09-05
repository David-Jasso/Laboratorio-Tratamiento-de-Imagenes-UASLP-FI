import cv2 as cv
import os
#Criterios para determinar algoritmo de cornerSubPix (Epsilon <= 0.001 e Iteraciones maximas = 30)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def detectar_tablero(img, grayImg, criteria, boardDimension):
    # Encontrar las esquinas del tablero de ajedrez.
    ret, corners = cv.findChessboardCorners(grayImg, boardDimension, flags = cv.CALIB_CB_FAST_CHECK)

    # Si son encontradas, refinar las esquinas y diujarlas en la imagen a color.
    if ret:
        # Ajustar y dibujar las esquinas con mayor precision.
        corners1 = cv.cornerSubPix(grayImg, corners, (3, 3), (-1, -1), criteria)
        cv.drawChessboardCorners(img, boardDimension, corners1, ret)

    return img, ret

def main():
    # Dimensiones de tablero en base a cual se este utilizando
    CHESS_BOARD_DIM = (6, 4)

    n = 0
    # La ruta del directorio de imágenes.
    image_dir_path = "images2"

    # Comprobar si el directorio ya existe en la ruta de archivos.
    CHECK_DIR = os.path.isdir(image_dir_path)
    if not CHECK_DIR:
        os.makedirs(image_dir_path) # Crea un directorio
        print(f'"{image_dir_path}" directorio ha sido creado')
    else:
        print(f'"{image_dir_path}" directorio ya existe')

    # Captura de video.
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)

    while True:
        _, frame = cap.read()
        copyFrame = frame.copy()
        # Conversion de fotograma a escala de grises.
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Llamada a funcion para detectar las esquinas del tablero de agedrez.
        image, board_detected = detectar_tablero(frame, gray, criteria, CHESS_BOARD_DIM)
        # Agregar texto indicando la imagen guardada.
        cv.putText(frame, f"Imagen guardada #{n}", (30,40), cv.FONT_HERSHEY_PLAIN, 1.4, (0, 255, 0), 2, )

        # Mostrar resultados.
        cv.imshow("Deteccion de tablero de ajedrez", frame)
        cv.imshow("Original", copyFrame)

        key = cv.waitKey(1)

        if key == ord('q'): break

        # Guardar resultado en el directorio creado.
        if key == ord('s') and board_detected == True:
            cv.imwrite(f"{image_dir_path}/image{n}.png", copyFrame)

            print(f"Numero de imagen: #{n}")
            n += 1

    cap.release()
    cv.destroyAllWindows()

    print("Total de imagenes guardadas:", n)

if __name__ == '__main__':
    main()
