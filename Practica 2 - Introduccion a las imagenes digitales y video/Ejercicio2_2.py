import cv2 as cv

#Lectura de video guardado en el dispositivo
vidCap = cv.VideoCapture('Recursos/traffic.mp4')

while(vidCap.isOpened()):
    ret, frame = vidCap.read() #Obtencion de los fotogramas
    #Si se esta capturando el video
    if ret: 
        cv.imshow('Ventana 2.2', frame) #Mandamos a una ventana los fotogramas
        key = cv.waitKey(1)
        #Hasta que presionemos la tecla q
        if key == ord('q'):
            break
    else:
        break
vidCap.release()
cv.destrollAllWindows()