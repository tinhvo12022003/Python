import requests as req
from bs4 import BeautifulSoup
import json

#bài tập 1
url = "http://www.bu.edu/president/boston-university-facts-stats/"

reponse = req.get(url)
text = reponse.text
soup = BeautifulSoup(text, "html.parser")
data = {
    'link' : [a['href'] for a in soup.find_all('a')],
    'text' : [p.get_text() for p in soup.find_all('p')],
    'title' : soup.title.string
}

with open('scraped_data.json', 'w') as file:
    json.dump(data, file, indent=4)

#bài tập 2

url = 'https://archive.ics.uci.edu/ml/datasets.php'
reponse = req.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')
table = {
    'table' : [str(table) for table in soup.find_all('table')]
}

with open('scraped_data.json', 'w', encoding='utf-8') as file:
    json.dump(table, file, indent=4)

#bài tập 3
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
reponse = req.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')
table = soup.find('table', class_='wikitable')
table_data = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    name = columns[1].text.strip()
    party = columns[4].text.strip()
    table_data.append({'name': name, 'party': party})

with open('scraped_data_table.json', 'w', encoding='utf-8') as file:
    json.dump(table_data, file, indent=4)
