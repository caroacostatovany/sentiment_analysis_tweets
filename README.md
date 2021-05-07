## Análisis de sentimientos en Tweets
________________

### Objetivo

El objetivo de este trabajo es construir un clasificador que aprenda a distinguir entre tweets positivos o negativos. 

- El documento que describe todo el presente trabajo, lo encuentras en este repositorio [documentacion/Artículo_final.pdf](https://github.com/ElenaVillano/sentiment_analysis_tweets/blob/main/documentacion/Art%C3%ADculo_final.pdf).
- La presentación que utilizada en [documentacion/Presentación.pdf](https://github.com/ElenaVillano/sentiment_analysis_tweets/blob/main/documentacion/Presentaci%C3%B3n.pdf). 

### Datos

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

- La variable que utilizaremos para entrenar es `text`, y como etiqueta `target`.

### Limpieza de texto

Para instalar nuestro paquete de limpieza de tweets:
> pip install "git+https://github.com/ElenaVillano/sentiment_analysis_tweets.git#egg=nlptweet&subdirectory=src"

### Modelos

El código lo puedes observar en la carpeta de notebooks, que viene desde la implementación de la limpieza, hasta ejemplos de los mejores modelos. 

### Algunas referencias:
- [Clasificación de texto para análisis de sentimiento con el clasificador Naive Bayes](https://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/)
- [Análisis de sentimientos en Twitter utilizando python y NLTK](http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)
- [Aprendizaje de máquina con H20, Twitter y python](https://www.linkedin.com/pulse/social-machine-learning-h2o-twitter-python-marios-michailidis/)

### Requerimientos
________________

Utilizaremos **python** y por ahora nuestros notebooks serán probados en `Google Colab`.




