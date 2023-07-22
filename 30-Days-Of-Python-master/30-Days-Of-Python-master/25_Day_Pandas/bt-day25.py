import pandas as pd

#bài tập 1
path = '30-Days-Of-Python-master/30-Days-Of-Python-master/data/hacker_news.csv'
df = pd.read_csv(path)
print(df)

#bài tập 2
print(df.head(5))

#bài tập 3
print(df.tail(5))

#bài tập 4
pandas_series = df['title']
print(pandas_series)

#bài tập 5
number_columns = df.shape[1]
number_rows = df.shape[0]

print('Number of rows: {}'.format(number_rows))
print('Number of columns: {}'.format(number_columns))

python_titles = df[df['title'].str.contains('python', case=False)]
print(python_titles)

javascript_titles = df[df['title'].str.contains('JavaScript', case=False)]
print(javascript_titles)