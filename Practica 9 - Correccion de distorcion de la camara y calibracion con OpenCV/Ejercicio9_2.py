import cv2 as cv
import numpy as np
import os

CHESS_BOARD_DIM = (6, 4)
SQUARE_SIZE = 14

# Criterios para determinar algoritmo de cornerSubPix (Epsilon <= 0.001 e Iteraciones maximas = 30)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

calib_data_path = "calib_data"
CHECK_DIR = os.path.isdir(calib_data_path)
if not CHECK_DIR:
    os.makedirs(calib_data_path)
    print(f'"{calib_data_path}" directorio ha sido creado.')
else:
    print(f'"{calib_data_path}" directorio ya existe.')

# preparar los puntos del objeto, como (0,0,0), (1,0,0), (2,0,0) ....,(7,5,0)
obj_3D = np.zeros((CHESS_BOARD_DIM[0] * CHESS_BOARD_DIM[1], 3), np.float32)
obj_3D[:, :2] = np.mgrid[0 : CHESS_BOARD_DIM[0], 0 : CHESS_BOARD_DIM[1]].T.reshape(-1, 2)
obj_3D *= SQUARE_SIZE

# Matrices para almacenar los puntos objeto y los puntos imagen de todas las imágenes.
obj_points_3D = [] # Puntos 3D en el espacio del mundo real
img_points_2D = [] # Puntos 2D en el plano de la imagen.

# La ruta del directorio de imágenes
image_dir_path = "images2"

files = os.listdir(image_dir_path)
for file in files:
    print(file)
    imagePath = os.path.join(image_dir_path, file)
    # print(imagePath)

    image = cv.imread(imagePath)
    # Conversion de fotograma a escala de grises.
    grayyScale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # Encontrar las esquinas del tablero de ajedrez.
    ret, corners = cv.findChessboardCorners(image, CHESS_BOARD_DIM, None)
    if ret == True:
        #Agregar los puntos en el espacio al arreglo.
        obj_points_3D.append(obj_3D)
        # Ajustar y dibujar las esquinas con mayor precision.
        corners2 = cv.cornerSubPix(grayyScale, corners, (3,3), (-1,-1), criteria)
        #Agregar las esquinas ajustadas al arreglo.
        img_points_2D.append(corners2)

# Funcion para calibracion de camara
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(obj_points_3D, img_points_2D, grayyScale.shape[::-1], None, None)
print("CALIBRADA")

print("Guardando los datos en un fichero utilizando Numpy")
np.savez(
    f"{calib_data_path}/MultiMatrix2",
    camMatrix = mtx,
    distCoef = dist,
    rVector = rvecs,
    tVector = tvecs,
)