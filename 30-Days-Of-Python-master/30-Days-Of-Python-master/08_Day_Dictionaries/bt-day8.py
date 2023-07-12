#bài tập 1
dog = {}

# bài tập 2
dog = {'name': 'Max', 'color': 'black', 'breed': 'German Shepherd', 'age': 5}

# bài tập 3
student = {
    'first_name': 'John', 
    'last_name': 'Doe', 
    'age': 30, 
    'gender': 'male',
    'marital_status': 'single',
    'skill': ['Python', 'Java', 'JavaScript'],
    'country': 'America',
    'city': 'New York',
    'address': '123 Main Street'
    }

# bài tập 4
print(len(student))

# bài tập 5
print(type(student['skill']))

# bài tập 6
student['skill'].append('C++')
print(student['skill'])

# bài tập 7
key_lst = student.keys()
print(key_lst)

# bài tập 8
value_lst = student.values()
print(value_lst)

# bài tập 9
dic_to_tp = student.items()
print(dic_to_tp)

# bài tập 10
student.pop('city')
print(student)

# bài tập 11
del student