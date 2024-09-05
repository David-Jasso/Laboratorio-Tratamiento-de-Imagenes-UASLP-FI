import cv2 as cv

#Captura de video del computador
cam = cv.VideoCapture(0, cv.CAP_DSHOW)

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret:
       cv.imshow('Ventana 2.3', frame) #Mostrar fotogramas en la ventana
       key = cv.waitKey(1)
       #Finalizamos el video al presionar la tecla ESC
       if key == 27: 
         break
    else:
        break
cam.release()
cv.destrollAllWindows()