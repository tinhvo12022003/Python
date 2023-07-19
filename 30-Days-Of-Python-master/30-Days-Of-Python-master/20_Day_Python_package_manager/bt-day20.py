import requests 
import re
import os
import math
import string
import numpy as np
#bài tập 1
from bs4 import BeautifulSoup  

def most_frequent_words(text):
    words = re.sub('r[^a-zA-Z0-9]', '', text).split()
    words = " ".join(words)
    str_txt = words.translate(str.maketrans('', '', string.punctuation))
    txt_dict = {}
    for word in str_txt.split():
        if word not in txt_dict:
            txt_dict[word] = 1
        else:
            txt_dict[word] += 1
    return sorted(txt_dict.items(), key=lambda x: x[1], reverse=True)[:10]
url = 'http://www.gutenberg.org/files/1112/1112.txt'

reponse = requests.get(url)
text = reponse.text

#bàu tập 2
url = 'https://api.thecatapi.com/v1/breeds'
def get_cat_weight(url):
    reponse = requests.get(url)
    cats = reponse.json()
    weight = []
    for cat in cats:
        weight.append(float(cat['weight']['metric'].split()[0]))
    return weight

cat_weight = get_cat_weight(url)
max_weight = max(cat_weight)
min_weight = min(cat_weight)
mean_weight = np.mean(cat_weight)
median_weight = np.median(cat_weight)
standard_deviation = np.std(cat_weight)

def get_lifespan(url):
    reponse = requests.get(url)
    reponse_json = reponse.json()
    lifespan = []
    for span in reponse_json:
        lifespan.append(float(span['life_span'].split()[0]))
    return lifespan
cat_lifespan = get_lifespan(url)
max_lifespan = max(cat_lifespan)
min_lifespan = min(cat_lifespan)
mean_lifespan = np.mean(cat_lifespan)
median_lifespan = np.median(cat_lifespan)
standard_deviation_lifespan = np.std(cat_lifespan)

def frequency_cats(url):
    reponse = requests.get(url)
    cats = reponse.json()
    origin = {}
    for cat in cats:
        if cat['origin'] not in origin:
            origin[cat['origin']] = 1
        else:
            origin[cat['origin']] += 1
    return origin.items()

def breed_cats(url):
    reponse = requests.get(url)
    cats = reponse.json()
    name = {}
    for cat in cats:
        if cat['name'] not in name:
            name[cat['name']] = 1
        else:
            name[cat['name']] += 1
    return name.items()
    

