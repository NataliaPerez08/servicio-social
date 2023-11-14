#  Red neuronal convolucional

Una red neuronal convolucional es un tipo de red neuronal artificial donde las neuronas artificiales, corresponden a campos receptivos de una manera muy similar a las neuronas en la corteza visual primaria (V1) de un cerebro biológico. Este tipo de red es una variación de un perceptron multicapa, sin embargo, debido a que su aplicación es realizada en matrices bidimensionales, son muy efectivas para tareas de visión artificial, como en la clasificación y segmentación de imágenes, entre otras aplicaciones.

Neuronas de Clasificación

Después de una o más fases de extracción de características, los datos finalmente llegan a la fase de clasificación. Para entonces, los datos han sido depurados hasta una serie de características únicas para la imagen de entrada, y es ahora la labor de esta última fase el poder clasificar estas características hacia una etiqueta u otra, según los objetivos de entrenamiento.

Las neuronas en esta fase funcionan de manera idéntica a las de un perceptron multicapas, donde la salida de cada una se calcula de esta forma:

$\displaystyle{y_{j}=g\left(b_{j}+\sum _{i}w_{ij}\cdot y_{i}\right)}$

Donde la salida y j ${\displaystyle y_{j}}$ de una neurona j j es un valor que se calcula por medio de la combinación lineal de las salidas y i y_{i} de las neuronas en la capa anterior cada una de ellas multiplicadas con un peso w i j ${\displaystyle w_{ij}}$ correspondiente a esa conexión. Esta cantidad es sumada a una influencia b j {\displaystyle b_{j}} y luego se pasa por una función de activación g ( ⋅ ) {\displaystyle g(\cdot )} no-lineal. 