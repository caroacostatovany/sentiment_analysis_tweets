## Análisis de sentimientos en Tweets
________________

### 1. Objetivo

El objetivo de esta práctica es construir un clasificador que aprenda a distinguir entre tweets serios o negativos y positivos. 

### 2. EDA datos

Los datos que utilizaremos fueron datos recolectados de twitter acerca del Huracán Harvey y tweets con intención negativa o seria.
- **Fuente**: [Referencia 1](https://www.linkedin.com/pulse/social-machine-learning-h2o-twitter-python-marios-michailidis/), [Referencia 2](https://www.kaggle.com/kazanova/sentiment140).
- **Número observaciones**: 1,600,000.
- **Variables**:
	- `target`: Polaridad del tweet, positivo o negativo.
	- `ids`: ID tweet.
	- `date`: Fecha y hora del tweet.
	- `flag`: Si hubo algún tipo de QUERY.
	- `user`: Usuario del tweet
	- `text`: Texto del tweet.
- **Variable característica**: `text`.
- **Variable etiqueta**: `target`.

#### Información general sobre variables:

- `target`: 50\% de las observaciones pertenecen a la categoría POSITIVO y 50\% a NEGATIVO.
- `ids`: 1,598,315 de los identificadores son únicos.
- `date`: El formato de esta variable es como el siguiente: `Mon Apr 06 22:19:45 PDT 2009`.
- `flag`: Todas sus observaciones tienen `NO_QUERY`.
- `user`: Tenemos 659,775 usuarios únicos.
- `text`: Se realizarán análisis de frecuencia de palabras para cada etiqueta. 



### 3. Modelos a utilizar (NLP).

Para este proyecto construiremos un modelo con base en procesamiento del Lenguaje Natural (NLP por sus siglas en inglés) para realizar análisis de sentimiento (en los data (tweets) de...) y clasificar si el sentimiento es positivo o negativo. 

Se aplicará un preprocesamiento a los datos para estandarizarlos, quitar stopwords, espacios en blanco, caracteres especiales y lematizarlos con el objetivo de mejorar el procesamiento del modelo y su aprendizaje.

¿Qué es Natural Language Processing? 

El Procesamiento del Lenguaje Natural (NLP por sus siglas en inglés) es el campo de estudio que se enfoca en la comprensión del lenguaje humano mediante una computadora o varias conectadas entres si (Clusters). Siendo una rama de la Inteligencia Artificial (Aprendizaje profundo), engloba parte de la Ciencia de Datos y la lingüística. 

En NLP las computadoras analizan el lenguaje humano, lo interpretan y dan significado para que pueda ser utilizado de manera práctica. Se listan algunas actividades que se pueden realizar al usar NLP tales como resumen automático de textos, traducción de idiomas, extracción de relaciones, reconocimiento del habla, clasificación de artículos por temáticas o usos, análisis de sentimiento, etc.


### 4. Trabajos relacionados

#### 4.1 Clasificación de texto para análisis de sentimiento con el clasificador Naive Bayes

En este [trabajo](https://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/) 
se enfocaron en la clasificación de sentimientos positivos o negativos, para mantener simplicidad. Utilizaron los datos 
que vienen en el paquete de NLTK para el corpus de reviews de películas.
Empezaron utilizando un simple **clasificador de Naive Bayes** como baseline, utilizando la extracción de variables de 
forma booleana. 
Con poca manipulación de los datos lograron obtener una exactitud de 73%, lo cual es cerca de la exactitud humana; se 
dice que los humanos concuerdan en sentimientos sólo el 80% del tiempo.

#### 4.2 Análisis de sentimientos en Twitter utilizando python y NLTK

El objetivo de este [proyecto](http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/) es 
clasificar un tweet positivo o negativo. Utilizó datos que extrajo manualmente, y fueron alrededor de 600 tweets 
positivos y 600 tweets negativos para el entrenamiento del clasificador, utilizó tweets sin hashtags, menciones o 
emojis.
La única imputación que realizó fue eliminar las palabras menores de 2 letras y tener todo en minúsculas. 
Para crear el clasificador, primero se hizo una extracción de variables para saber cuáles eran las variables 
relevantes; y el clasificador utilizado fue **Naives Bayes de NLTK**. Con sus datos de prueba lograron un 80% de
exactitud.

#### 4.3 Aprendizaje de máquina con H20, Twitter y python

La idea de este [proyecto](https://www.linkedin.com/pulse/social-machine-learning-h2o-twitter-python-marios-michailidis/)
es extraer tweets relevantes para el caso del huracán Harvey, utilizando el dataset de 'sentiment140' que ya estan 
etiquetados como sentimientos positivos o negativos, después construir un clasificador que aprenda a diferenciar entre 
un tweet negativo o serio y un tweet positivo; posterioremente utilizar este clasificador para rankear los tweets 
basados en un porcentaje de severidad y así poder extraer el top de tweets que necesiten ayuda en la situación actual, 
en este caso, el Huracán Harvey o Irma.
Para la transformación de sus datos utilizaron **TF-IDF**, éste extrae para cada palabra qué tan importante es para 
ese tweet. 
Después de la transformación, utilizaron **H20 Gradient Boosting** para entrenar y obtener el clasificador que 
diferencíe entre un tweet positivo o negativo. 


# Referencias
- [Clasificación de texto para análisis de sentimiento con el clasificador Naive Bayes](https://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/)
- [Análisis de sentimientos en Twitter utilizando python y NLTK](http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)
- [Aprendizaje de máquina con H20, Twitter y python](https://www.linkedin.com/pulse/social-machine-learning-h2o-twitter-python-marios-michailidis/)

# Requerimientos
________________

Utilizaremos **python** y por ahora nuestros notebooks serán probados en `Google Colab`.


