import requests
from bs4 import BeautifulSoup
import re
import os

base_url = "https://www.letras.mus.br"


def extract_lyrics(href):
    full_url = base_url + href

    response = requests.get(full_url, timeout=10)

    soup = BeautifulSoup(response.text, 'html.parser')

    div_lyric = soup.find('div', class_='lyric-original')

    return div_lyric.get_text(separator="\n").strip()


response = requests.get(f"{base_url}/mais-acessadas/funk/", timeout=10)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')

top_list_element = soup.find(class_='top-list_mus --top')

for child in top_list_element.find_all('li'):
    a_tag = child.find('a')

    title = a_tag['title']
    title = re.sub(r'[\/:*?"<>|]', '_', title)
    title = f"lyrics/{title}.txt"

    print(f"Obtendo {a_tag['title']}")

    if os.path.exists(title):
        print(
            f"Arquivo para '{title}' já existe. Pulando para a próxima música.")

        continue

    if a_tag and 'href' in a_tag.attrs:

        with open(title, 'w', encoding='utf-8') as file:
            file.write(extract_lyrics(a_tag['href']))
