import cv2 as cv

img = cv.imread('Recursos/Hollow Knight.jpg')
img= cv.resize(img, None, fx = 0.5, fy = 0.5)

r = cv.selectROI('Seleccionar el area', img)

print(r)

img_roi = img[int(r[1]):int(r[1] + r[3]),
              int(r[0]):int(r[0] + r[2])]
            
while True:
    cv.imshow('Ventana 4.2', img_roi)

    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()