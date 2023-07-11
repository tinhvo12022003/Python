it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

            #LEVEL 1

#Bài tập 1
print(len(it_companies))

#Bài tập 2
#type 1
it_companies.update({'Twitter'})
print(it_companies)
#type 2
it_companies.add('Twitter')
print(it_companies)

#Bài tập 3
it_companies.update({'OpenAI', 'FireFox', 'Samsung'})
print(it_companies)

#Bài tập 4
it_companies.remove('Apple')
print(it_companies)

#Bài tập 5
'''
Tóm lại, remove() và discard() đều được sử dụng để xóa phần tử khỏi set,
nhưng remove() sẽ ném ra lỗi nếu phần tử không tồn tại trong set,
trong khi discard() sẽ không làm gì nếu phần tử không tồn tại.
'''

                #LEVEL 2
#Bài tập 1
C = A.union(B)
print(C)

#Bài tập 2
print(A.intersection(B)) #output: {19, 20, 22, 24, 25, 26}

#Bài tập 3
print(A.issubset(B)) #output: True

#Bài tập 4
print(A.isdisjoint(B)) #output: false

#Bài tập 5
C = A.union(B)
D = B.union(A)

#Bài tập 6
print(A.symmetric_difference(B))

#Bài tập 7
del A, B, C, D

                #LEVEL 3
#Bài tập 1
age_set = set(age)
print(len(age_set), len(age))

#Bài tập 3
text = 'I am a teacher and I love to inspire and teach people'
print(len(set(text.split(' '))))
