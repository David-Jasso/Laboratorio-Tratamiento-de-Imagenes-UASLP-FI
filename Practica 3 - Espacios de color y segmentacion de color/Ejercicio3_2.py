import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Función para mostrar las imagenes con pyploy.
def plot_img(images, titles):
  fig, axs = plt.subplots(nrows = 1, ncols = len(images), figsize = (20, 20))
  for i, p in enumerate(images):
    axs[i].imshow(cv.cvtColor(p, cv.COLOR_BGR2RGB))
    axs[i].set_title(titles[i])
    axs[i].axis('off')
  plt.show()

img = cv.imread('Imagenes/Stardew Valley.jpg')
#Conversión de espacio de color de BGR a HSV.
img2 = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Separar el valor de cada canal del espacio HSV.
h, s, v = cv.split(img2)

#Aumentamos el canal Valor en 50.
canal_v = v + 50

#Agregamos el nuevo valor del canal Valor
#A la tupla del espacio de color HSV.
img3 = cv.merge([h, s, canal_v])

imagenes = [img, img3]
titulos = ['Original', 'Canal V aumentado']

plot_img(imagenes, titulos)
imagenes.clear()
titulos.clear()