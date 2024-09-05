import cv2 as cv

def main():
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    primera_cap = False
    segunda_cap = False

    while True:
        ret, frame = cap.read()
        cv.imshow('Video', frame)
        key = cv.waitKey(1) 
        if (key == ord('u')) and (not primera_cap):
            cv.imwrite('Laboratorio TI/Practica 7 - Umbralizacion y operaciones morfologicas/Imagenes/una.png', frame)
            primera_cap = True
            frame = cv.resize(frame, None, fx = 0.4, fy = 0.4)
            cv.imshow('Fondo', frame)

        elif (key == ord('d')) and primera_cap:
            cv.imwrite('Laboratorio TI/Practica 7 - Umbralizacion y operaciones morfologicas/Imagenes/dos.png', frame)
            segunda_cap = True
            frame = cv.resize(frame, None, fx = 0.4, fy = 0.4)
            cv.imshow('Objeto', frame)

        elif (key == ord('w')) and primera_cap and segunda_cap:
            cv.destroyAllWindows()
            cap.release()

            bck = cv.imread('Laboratorio TI/Practica 7 - Umbralizacion y operaciones morfologicas/Imagenes/una.png')
            top = cv.imread('Laboratorio TI/Practica 7 - Umbralizacion y operaciones morfologicas/Imagenes/dos.png')

            mascaras = deteccion_dif(bck, top)

            cv.waitKey(0)
            cv.destroyAllWindows()

            b, g, r = cv.split(top)
            for i, msk in enumerate(mascaras):
                b = cv.bitwise_and(b, msk)
                g = cv.bitwise_and(g, msk)
                r = cv.bitwise_and(r, msk)
                seg = cv.merge((b, g, r))
                cv.imshow('Segmentada mascara {}', format(i), seg)

            cv.waitKey(0)
            break

        elif key == ord('q'):
            break
    
    cv.destroyAllWindows()

def deteccion_dif(prev, curr):
    prevG = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
    currG = cv.cvtColor(curr, cv.COLOR_BGR2GRAY)

    diff_frame = cv.subtract(currG, prevG)
    cv.imshow('Diferencia', diff_frame)
    cv.waitKey(5000)
    cv.destroyWindow('Diferencia')

    thresh = cv.threshold(diff_frame, 40, 255, cv.THRESH_BINARY)[1]
    cv.imshow('Umbralizado de diferencia', thresh)
    cv.waitKey(5000)
    cv.destroyWindow('Umbralizado de diferencia')

    k3 = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mask1 = cv.dilate(thresh, k3, iterations=3)
    cv.imshow('Dilatacion', mask1)
    mask2 = cv.erode(thresh, k3, iterations=3)
    cv.imshow('Erosion', mask2)
    mask3 = cv.morphologyEx(thresh, cv.MORPH_OPEN, k3, iterations= 3)
    cv.imshow('Apertura', mask3)
    mask4 = cv.morphologyEx(thresh, cv.MORPH_CLOSE, k3, iterations= 3)
    cv.imshow('Cierre', mask3)

    return [mask1, mask2, mask3, mask4]

if __name__ == '__main__':
    main()