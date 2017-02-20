##Projeto - Visão 2

### Descrição
Utilizando OpenCV, detectar três círculos alinhados, retornar sua distância e a sua orientação.


### Metas
- [x] Detecta somente os círculos desejados.
- [X] Imprime a quantidade de círculos detectada
- [x] Imprime a distância correta dos três círculos visíveis.
- [x] Imprime a orientação dos círculos alinhados: horizontal, vertical e inclinado.
- [ ] Excluí circulos de diferentes raios e/ou não tem centros colineares.
- [ ] Mostra a imagem do John Travolta quando não há nennum círculo detectado
- [ ] Vídeo demonstração
- [X] Documentação do projeto

### Detalhes
- No OpenCV há uma função chamada HoughCircles, que detecta circulos na imagem dada, dependendo dos parâmentros.
```
	cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
```

| Parâmetros | Descrição |
| --- | --- |
| `image` | imagem a ser analisada. Neste caso, usamos o video da webcam |
| `method` | método a ser usado para detectar os círculos. Neste caso, o usado foi cv2.HOUGH_GRADIENT |
| `dp` | "Este parâmetro é a razão inversa da resolução do acumulador para a resolução da imagem (ver [Yuen et al](http://www.bmva.org/bmvc/1989/avc-89-029.pdf) para mais detalhes). Essencialmente, quanto maior for o dp, menor será a matriz do acumulador, isto é, mais círculos serão detectados" |
| `minDist` | menor distância dos centros (x,y) entre os círculos detectados |
| `param1` | irrelevante para o projeto |
| `param2` | irrelevante para o projeto |
| `minRadius` | tamanho mínimo do raio do circulo a ser detectado |
| `maxRadius` | tamanho máximo do raio do circulo a ser detectado |

- A função HoughCircles devolve uma matriz contendo a posição **X** e **Y** do centro dos círculos, assim como o seus **raios**.
```
	[[534,201,50],[424,124,52],[523,153,48]]
```

- A partir das coordenadas de centro dos círculos, é possível verificar se eles estão alinhados verticalmente ou horizontalmente. Se as coordenadas X dos círculos estiverem próximas, podemos inferir que eles estão verticalmente alinhado. Caso as coordenadas Y estiverem próximas, podemos concluir que os círculos estão horizontalmente alinhados.

#### Calculando a distância do círculo à tela:
Para calcular a distância, era necessário obter o foco da webcam, utilizando os [princípios da óptica](http://s2.glbimg.com/gdm71wKsRXN87Z3QJQenowTRYHU=/0x0:405x220/400x217/s.glbimg.com/po/ek/f/original/2014/01/07/figura_8.jpg). Para isso, foi preciso medir a distância do círculo até a câmera, o tamanho da imagem do círculo [obtida](https://i.gyazo.com/2e9c2ba0610f926625c4123f4ab35e2f.png) pela câmera e o raio real do círculo. Tendo estas informações e aplicando a regra de três, obteve-se que o foco da câmera é aproximadamente 11.

Tendo em mãos o foco da câmera, a variável passa a ser a distância entre a câmera e o círculo, dada por:
```
	distancia = foco * raio real em pixels / raio imagem em pixels
```

