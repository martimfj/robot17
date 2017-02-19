import cv2
import cv2.cv as cv
import numpy as np
from matplotlib import pyplot as plt
import time


cap = cv2.VideoCapture(1) # 1 = webcam frontal, 0 webcam traseira
f = 10.945 #foco
h = 3*37.795672 #raio do circulo real em pixels
font = cv2.FONT_HERSHEY_SIMPLEX


while True:
	ret, img = cap.read() #define a "imagem" que o codigo vai iterar
	image =cv2.GaussianBlur(img,(5,5),10)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1.2, 100,minRadius=5,maxRadius=230) 
	#matriz de circulos detectados por milisegundo. [x, y, raio]

	if circles is None:
		msg = "Nenhum circulo detectado"
		cv2.putText(img,msg,(100,100), font, 1,(0,0,255),2)
		# travolta = cv2.imread("travolta.png")
		# plt.imshow('travolta', travolta)
		msg1 = "Pressione Q para sair"
		cv2.putText(img,msg1,(140,450), font, 1,(255,255,255),2)

	else:
		circles = np.round(circles[0, :]).astype("int") #arredonda os numeros da matriz como int
		verf_x = np.arange(circles[0][0]-10,circles[0][0]+10,1) #lista de verificacao vertical, alcance de 20
		verf_y = np.arange(circles[0][1]-10,circles[0][1]+10,1) #lista de verificacao horizontal, alcance de 20 

		for (x, y, r) in circles: #percorre a matriz de circulos detectados
			cv2.circle(img, (x, y), r, (255, 0, 255), 4) #desenho do circulo detectado
			cv2.circle(img, (x, y), 5, (0, 255, 255), -1) #desenho do centro do circulo detectado
			#cv2.circle(img, centro, raio, cor, espessura)

			for i in range (len(circles)):
				for j in range (len(circles[i])):
					if circles[i][1] in (verf_y): 
						orientacao = "Horizontal"
					#Se a coordenada Y do centro do circulo estiver na lista verf_y, ela esta alinhada horizontalmente com outro circulo
					elif circles[i][0] in (verf_x):
						orientacao = "Vertical"
						#Se a coordenada X do centro do circulo estiver na lista verf_x, ela esta alinhada verticalmente com outro circulo
					else:
						orientacao = "Inclinado"
						#caso nao esteja alinhado esta inclinado

		dist = "Distancia da tela: {} cm".format(np.round(f*h/r))

		cv2.putText(img,str(dist),(50,100), font, 1,(0,0,255),2)
		cv2.putText(img,orientacao,(50,50), font, 1,(0,255,0),2)
	
	cv2.imshow("output", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break  
cap.release()
cv2.destroyAllWindows()