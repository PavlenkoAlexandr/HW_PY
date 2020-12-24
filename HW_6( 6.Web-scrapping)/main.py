import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/all/'


def search_matches(text):
    for keyword in KEYWORDS:
        pattern = re.compile(f'{keyword}')
        if re.search(pattern, text):
            return True


def make_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


posts = make_soup(URL).find_all('article', class_='post')

for post in posts:

    post_elements = post.find(class_='post__title_link')
    head = post_elements.text
    link = post_elements.attrs.get('href')
    post_time = post.find(class_='post__time').text
    post_preview = post.find(class_='post__text').text

    match = search_matches(post_preview)

    if not match:
        text = make_soup(link).find(class_='post__text').text
        match = search_matches(text)
    if match:
        print(f'{post_time} - {head} - {link}')
