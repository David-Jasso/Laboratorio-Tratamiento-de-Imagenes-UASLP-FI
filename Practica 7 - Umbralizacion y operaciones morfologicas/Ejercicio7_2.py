import cv2 as cv

def main():
    vid_capture = cv.VideoCapture('Laboratorio TI/Practica 7 - Umbralizacion y operaciones morfologicas/Recursos/Calle.mp4')

    prev_frame = None

    while(vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        if ret:
            key = cv.waitKey(10)
            if key == ord('q'):
                break

            # Procesar fotograma actual para facilidad de deteccion
            prep_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            prep_frame = cv.GaussianBlur(prep_frame, (5, 5), 0)

            # Fijar el fotograma anterior y continuar si es el inicio del video
            if prev_frame is None:
                prev_frame = prep_frame
                continue

            # Funcion de deteccion de movimiento por resta
            mov_frame = deteccion_mov(prep_frame, prev_frame)
            prev_frame = prep_frame

            # Encontrar contornos y dibujar areas de movimiento
            contours, _ = cv.findContours(mov_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            cv.drawContours(frame, contours, -1, (0, 255, 0), 2, cv.LINE_AA)

            for cnt in contours:
                if cv.contourArea(cnt) < 50:
                    continue
                (x, y, w, h) = cv.boundingRect(cnt)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, cv.LINE_AA)
            cv.imshow('Video', frame)

        else:
            break
    
    vid_capture.release()
    cv.destroyAllWindows()

def deteccion_mov(curr, prev):
    # Calcular diferencia entre ambos fotogramas
    diff_frame = cv.absdiff(curr, prev)

    # Umbralizar las areas de mayor diferencia
    thresh_frame = cv.threshold(diff_frame, 20, 255, cv.THRESH_BINARY)[1]

    #Cerrar imagen un poco para hacer la diferencia más notable
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    diff_frame = cv.morphologyEx(thresh_frame, cv.MORPH_CLOSE, kernel, iterations=10)

    cv.imshow('Video', thresh_frame)
    return diff_frame

if __name__ == '__main__':
    main()