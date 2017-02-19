##Projeto - Visão 2

#### Descrição
Utilizando OpenCV, detectar três círculos alinhados, retornar sua distância e a sua orientação.


#### Metas
- [x] Detecta somente os círculos desejados.
- [x] Imprime a distância correta dos três círculos visíveis.
- [x] Imprime a orientação dos círculos alinhados: horizontal, vertical e inclinado.
- [ ] Excluí circulos de diferentes raios e/ou não tem centros colineares.
- [ ] Mostra a imagem do John Travolta quando não há nennum círculo detectado
- [ ] Vídeo demonstração
- [X] Documentação do projeto

#### Detalhes
- No OpenCV há uma função chamada HoughCircles, que detecta circulos na imagem dada, dependendo dos parâmentros.
'''
	circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1.2, 100,minRadius=5,maxRadius=230)
	#cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
'''
	> image: imagem a ser analisada. Neste caso, usamos o video da webcam
	> method: método a ser usado para detectar os círculos. Neste caso, o usado foi cv2.HOUGH_GRADIENT
	> dp: "Este parâmetro é a razão inversa da resolução do acumulador para a resolução da imagem (ver [Yuen et al](http://www.bmva.org/bmvc/1989/avc-89-029.pdf) para mais detalhes). Essencialmente, quanto maior for o dp, menor será a matriz do acumulador."
	> minDist: menor distância dos centros (x,y) entre os círculos detectados
	> param1: 
	> param2:
	> minRadius: tamanho mínimo do raio do circulo a ser detectado
	> maxRadius: tamanho máximo do raio do circulo a ser detectado

