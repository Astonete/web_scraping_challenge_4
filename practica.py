"""
Mini LiveCoding — Scraping Básico
=================================

Objetivo:
    - Completar el scraping.
    - Recorrer los primeros 5 libros.
    - Imprimir:
          Título | Precio

Reglas:
    - No hardcodear datos.
    - Usar select o select_one.
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"


def scrapear():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    libros = soup.select("article.product_pod")[:5]

    todo = {}
    # TODO 1:
    # Recorrer los libros seleccionados
    for libro in libros:
        titulo = libro.h3.a['title']
        price = libro.find('p',class_='price_color').get_text()
        todo["title"] = titulo
        todo["Precio"] = price

        # TODO 2:
        # Extraer:
        #   - title (desde h3 > a)
        #   - price (desde clase "price_color")

        # TODO 3:
        # Imprimir con formato:
        #   Título | Precio
        print(todo)
pass


if __name__ == "__main__":
    scrapear()