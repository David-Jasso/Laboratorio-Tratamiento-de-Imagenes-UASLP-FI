import cv2 as cv
import numpy as np
import time

def main():
    # Parametros para el algoritmo de flujo optico de Lucas Kanade
    lk_params = dict(winSize = (15,15),
                     maxLevel = 2,
                     criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
    
    # Parametros para el algoritmo de deteccion de esquinas Shi-Tomasi
    feature_params = dict(maxCorners = 20,
                          qualityLevel = 0.3,
                          minDistance = 10,
                          blockSize = 7)
    
    trajectory_len = 40 # Tamaño de trayectoria
    detect_interval = 5 # Intervalo de detección
    trajectories = [] # Arreglo para almacenamiento de trayectorias
    frame_idx = 0 # Contador para fotogramas

    # Cargar y leer el video de la carpeta de Recursos
    cap = cv.VideoCapture('Laboratorio TI/Practica 8 - Deteccion de esquinas y flujo optico/Recursos/slow_traffic_small.mp4')
    suc, frame_prev = cap.read()

    # Cambiar el tamaño de la ventana del frame
    frame_prev = cv.resize(frame_prev, None, fx = 0.5, fy = 0.5)

    # Convertir la imagen de entrada en espacio de color en escala de grises
    prev_gray = cv.cvtColor(frame_prev, cv.COLOR_BGR2GRAY)

    while True:
        # Lectura del video y cambio de tamaño de la ventana del frame
        ret, frame = cap.read()
        frame = cv.resize(frame, None, fx = 0.5, fy = 0.5)
        if ret:
            # Convertir la imagen de entrada en espacio de color en escala de grises
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            #Copiar el frame en la variable img
            img = frame.copy()

            # Si hay elementos en el arreglo
            if len(trajectories) > 0:
                img0, img1 = prev_gray, frame_gray
                # Vector de puntos 2D para los que se necesita encontrar el flujo optico dispero
                p0 = np.float32([trajectory[-1] for trajectory in trajectories]).reshape(-1, 1, 2)

                # Calculo del flujo optico disperso para el frame anterior, puntos anteriores y frame actual
                p1, _st, _err = cv.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)

                # Calculo del flujo optico disperso para el frame anterior, puntos anteriores y frame actual
                p0r, _st, _err = cv.calcOpticalFlowPyrLK(img0, img1, p1, None, **lk_params)

                # Diferencia del flujo optico actual y anterior
                d = abs(p0-p0r).reshape(-1, 2).max(-1)

                # Criterio de seleccion de buenos puntos
                good = d < 1

                # Arreglo para almacenar las trayectorias con los puntos buenos
                new_trajectories = []

                # Agregar las trayectorias a un nuevo arreglo si los puntos son buenos
                for trajectory, (x, y), good_flag in zip(trajectories, p1.reshape(-1,2), good):
                    if not good_flag:
                        continue
                    trajectory.append((x, y))
                    if len(trajectory) > trajectory_len:
                        del trajectory[0]
                    new_trajectories.append(trajectory)

                    # Dibujar un circulo en las esquinas de los objetos
                    cv.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)
                
                #Actualizar trayectorias
                trajectories = new_trajectories
                
                # Mostrar en la ventana las trayectorias y el conteo de estas.
                cv.polylines(img, [np.int32(trajectory) for trajectory in trajectories], False, (0, 255, 0))
                cv.putText(img, 'track count: %d' % len(trajectories), (20, 50), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

            if frame_idx % detect_interval == 0:
                # Encontrar las esquinas mas fuertes de cada frame
                p = cv.goodFeaturesToTrack(frame_gray, **feature_params)
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        trajectories.append([(x,y)])

            # Actualizar contador y fotogramas
            frame_idx += 1
            prev_gray = frame_gray

            # Mostrar en la ventana el resultado
            cv.imshow('Flujo Optico Disperso', img)

            if cv.waitKey(10) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
