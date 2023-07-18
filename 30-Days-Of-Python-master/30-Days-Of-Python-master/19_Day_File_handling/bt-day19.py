            #LEVEL 1
#bài tập 1
import re
import os
import string
import math
def count_WordsAnd_Lines(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        line_count = len(lines)
        
        words = " ".join(lines).split()
        return "Words: {}, Lines: {}".format(len(words), line_count)
file_path1 = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/obama_speech.txt'
file_path2 = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/michelle_obama_speech.txt'
file_path3 = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/ donald_speech.txt'
file_path4 = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/melina_trump_speech.txt'

#bài tập 2
import json
def most_spoken_languages(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data_json = json.loads(f.read())
        result = {}
        for data in data_json:
            for language in data['languages']:
                if language not in result:
                    result[language] = 1
                else:
                    result[language] += 1
        return sorted(result.items(), key=lambda x: x[1], reverse=True)[:10]
path = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/countries_data.json'


#bài tập 3
def most_populated_countries(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data_json = json.loads(f.read())
        countries_population = [{'country': data['name'], 'population': data['population']} for data in data_json]
        print(countries_population)
        return sorted(countries_population, key=lambda x: x['population'], reverse=True)[:10]


path = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/countries_data.json'
# print(most_populated_countries(path))

                #LEVEL 2
#bài tập 4
def emails_list(filepath):
    with open('30-Days-Of-Python-master/30-Days-Of-Python-master/data/email_exchanges_big.txt') as f:
        text = f.read()
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(pattern, text)
        return emails
# path = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/email_exchanges_big.txt'
# print(emails_list(path))

#bài tập 5 + 6
def find_most_common_word(filepath="", n=0):
    if filepath == "" or n == 0:
        print("Invalid")
    else:
        with open(filepath) as f:
            text = f.read().split()
            words = {}
            for word in text:
                word = re.sub('r[^a-zA-Z0-9]', '', word)
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[:n]


#bài tập 7
def clean_text(param):
    if os.path.exists(param):
        with open(param, 'r', encoding='utf-8') as f:
            text = f.read()
            text = re.sub('r[^a-zA-Z0-9]', '', text)
            return text.translate(str.maketrans('', '', string.punctuation))
    else: return param.translate(str.maketrans('', '', string.punctuation))

def remove_support_words(param): #as string
    return re.sub('r[^a-zA-Z0-9]', '', param)

def check_text_similarity(param1, param2):
    text1 = clean_text(param1)
    text2 = clean_text(param2)

    text1_lst = remove_support_words(text1)
    text2_lst = remove_support_words(text2)

    words1 = set("".join(text1_lst).split())
    words2 = set("".join(text2_lst).split())
    print(words1)
    print(words2)
    return round(len(words1.intersection(words2)) / len(words1.union(words2)) * 100, 4)

#bài tập 9
import csv
def read_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = csv.reader(f, delimiter=',')
        count_python = count_js = count_java = 0
        for row in text:
            if 'python' in row[1].lower():
                count_python += 1
                print(row)
            elif 'javascript' in row[1].lower():
                count_js += 1
            elif 'java' in row[1].lower() and 'javascript' not in row[1].lower():
                count_java += 1
    return "Python: {}, JavaScript: {}, Java: {}".format(count_python, count_js, count_java)            

path = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/hacker_news.csv'
print(read_csv(path))
