#see: https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
from setuptools import setup, find_packages

setup(name="nlp-limpieza",
      version="0.1",
      description=u"Paquete que contiene limpieza de texto para tweets",
      url="",
      author="elevillano, caroacostatovany",
      author_email="",
      license="MIT",
      packages=find_packages(),
      install_requires = [
                          "numpy",
                          "pandas",
                          "sphinx",
                          "nltk"
                          ],
      )