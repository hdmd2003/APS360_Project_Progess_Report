import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

np.random.seed(3)

url_list = []
# set this to the number of texts you want
for i in range(10):
    num = np.random.randint(64000)
    url_list.append('https://www.gutenberg.org/cache/epub/' + str(num) + '/pg' + str(num) + '-images.html')

titles = []
excerpts = []
for url in url_list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.title

    if isEnglish(title) == False:
        continue

    text = (' '.join([p.get_text(strip=True) for p in soup.select('body p')[2:]]))
    text = text.replace('\r', ' ')
    text = text.replace('\n', ' ')
    text = text.replace('\xa0', ' ')
    text = re.sub("\[.*?\]","", text)
    text = text.replace('  ', ' ')
    text = text.split('.')

    if(len(text) < 20):
        continue

    # get an excerpt from the middle of the text
    index = np.random.randint(len(text) // 10, 9 * len(text) // 10)

    excerpt = ''

    while len(excerpt.split(' ')) < 150:
        excerpt = excerpt + text[index]
        index = index + 1

    titles.append(title)
    excerpts.append(excerpt)