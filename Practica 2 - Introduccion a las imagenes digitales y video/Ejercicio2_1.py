import cv2

img = cv2.imread("Recursos/New_Zealand_Lake.jpg")

#Mostrar imagen durante 8 segundos
cv2.imshow('Ventana 2.1.1', img)
cv2.waitKey(8000)
cv2.destroyAllWindows('Ventana 2.1.1')

#Mostrar imagen hasta presionar una tecla
cv2.imshow('Ventana 2.1.2', img)
cv2.waitKey(0) 
cv2.destroyAllWindows('Ventana 2.1.2')

#Mostrar imagen hasta presionar la tecla q
mostrar = True
while mostrar:
   cv2.imshow('Ventana 2.1.3', img)
   keypress = cv2.waitKey(1) 
   if keypress == ord('q'):
      mostrar == False
cv2.destroyAllWindows('Ventana 2.1.3')
