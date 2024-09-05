import cv2 as cv
import numpy as np

def main():
    # Capturary leer el video
    cap = cv.VideoCapture(0)

    suc, prev = cap.read()
    #prev = cv.resize(prev, None, fx=0.5, fy=0.5)

    # Si la lectura de video es correcta
    if suc:
        # Convertir el frame anterior a escala de grises
        prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)

        while True:
            #Lectura de video
            ret, img = cap.read()
            #img = cv.resize(img, None, fx = 0.5, fy = 0.5)
            #Si la lectura de video es correcta
            if ret:
                # Convertir el frame actual a escala de grises
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

                # Calcular el flujo optico denso mediante el algoritmo de Gunner Farneback's
                flow = cv.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

                # Actualizar el frame
                prevgray = gray

                # Mostrar el flujo optico denso en escala de grises y en espacio de color HSV
                cv.imshow('Flow', draw_flow(gray, flow))
                cv.imshow('Flow HSV', draw_hsv(flow))

                key = cv.waitKey(5)
                if key == ord('q'):
                    break

            else:
                break

    cap.release()
    cv.destroyAllWindows()

#Función para dibujar el flujo optico en espacio de color BGR
def draw_flow(img, flow, step = 15):

    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y, x].T

    lines = np.vstack([x, y, x - fx, y - fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)

    img_bgr = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    cv.polylines(img_bgr, lines, 0, (0, 255, 0))

    for (x1, y1), (_x2, _y2) in lines:
        cv.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

    return img_bgr

#Función para dibujar el flujo optico en espacio de color HSV
def draw_hsv(flow):

    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]

    ang = np.arctan2(fy, fx)+ np.pi
    v = np.sqrt(fx*fy + fy*fy)

    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[..., 0] = ang*(180/np.pi/2)
    hsv[..., 1] = 255
    hsv[..., 2] = np.minimum(v*4, 255)
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    return bgr

if __name__ == '__main__':
    main()