"""
Módulo para hacer preprocesamiento de los datos
"""
import re as re
from nlp.utils.constants import NLTK_STOPWORDS, EXTRA_STOPWORDS


def convierte_a_minusculas(df):
    """
    Convierte a minúsculas todas las celdas de tipo str en un dataframe

    :param df: dataframe
    :return: dataframe en minúsculas
    ==========
    Ejemplo:
        >> dataframe = convierte_a_minusculas(dataframe)
    """

    df = df.applymap(lambda s: s.lower() if type(s) == str else s)

    return df


def separar_abreviaciones(phrase):
    """

    :param phrase:
    :return:
    """
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)

    return phrase


def remove_stopwords(phrase):
    """

    :param phrase:
    :return:
    """
    phrase = ' '.join(e.lower() for e in phrase.split() if e.lower() not in EXTRA_STOPWORDS)
    phrase = ' '.join(e.lower() for e in phrase.split() if e.lower() not in NLTK_STOPWORDS)
    return phrase


def reemplazar_urls(phrase):
    """

    :param phrase:
    :return:
    """
    return re.sub("((www\.[\S]+)|(https?://[\S]+))", "url", phrase)


def reemplazar_usuarios(phrase):
    """

    :param phrase:
    :return:
    """
    return re.sub("@[\S]+. 2", "user_mention", phrase)


def quitar_hashtag(phrase):
    """

    :param phrase:
    :return:
    """
    return re.sub("#(\S+)", "", phrase)


def quitar_RT(phrase):
    """

    :param phrase:
    :return:
    """
    return re.sub("\brt\b", "", phrase)


def quitar_caracteres_especiales(phrase):
    """

    :param phrase:
    :return:
    """
    caracteres_especiales = '’"?!,.():;-'
    # quita dobles espacios y lo hace 1
    phrase = re.sub(' +', ' ', phrase)
    # quita los caracteres especiales
    regex = re.compile('[%s]' % re.escape(caracteres_especiales))

    return regex.sub('', phrase)


def quitar_letras_repetidas(phrase):
    """

    :param phrase:
    :return:
    """
    return re.sub(r'(.)\1+', r'\1\1', phrase)


def quitar_nonascii(phrase):
    """

    :param phrase:
    :return:
    """
    return phrase.encode('ascii', errors='ignore').decode('utf-8')
