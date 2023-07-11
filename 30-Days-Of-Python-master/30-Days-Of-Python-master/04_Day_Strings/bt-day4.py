# bài tập 1
arr_str = ['Thirty', 'Days', 'Of', 'Python']
print(" ".join(arr_str))

# bài tập 2
arr_str = ['Coding', 'For', 'All']
print(" ".join(arr_str))

# bài tập 3
company = "Coding For All"

# bài tập 4
print(company)

# bài tập 5
print(len(company))

# bài tập 6
print(company.upper())

# bài tập 7
print(company.lower())

# bài tập 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# bài tập 9
print(company[company.index(" ") + 1:])

# bài tập 10
company = "Coding For All"
#method 1
print("True") if("Coding" in company) else print("False")
#method 2
print("True") if(company.find("Coding")) else print("False")
#method 3
try:
   index = company.index("Coding")
   print(index)
except ValueError as e:
   print(e)

# bài tập 11
print(company.replace("Coding", "Python"))

# bài tập 12
#type 1
print(company.replace("All", "Everyone"))
#type 2
import re
print(re.sub("All", "Everyone", company))

# bài tập 13
print(company.split(" "))

# bài tập 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# bài tập 15
print(company[0]) #ouput: 'C'

# bài tập 16
print(company[-1]) #ouput: 'l'

# bài tập 17
print(company[10]) #output: ' '

# bài tập 18
name = "Python For Everyone"
acronym = "".join(word[0] for word in name.split(" "))
print(acronym)
#hay

# bài tập 19
name = "Coding For All"
acronym = "".join(word[0] for word in name.split(" "))
print(acronym)

# bài tập 20
print(name.index('C'))

# bài tập 21
print(name.index('F', 6, 14))

# bài tập 22
name = "Coding For People"
print(name.rfind('l'))

# bài tập 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
#type 1
print(sentence.index("because"))
#type 2
print(sentence.find("because"))

# bài tập 24
print(sentence.rfind("because"))

# bài tập 25
#type 1
print(sentence[: + sentence.index('because'):] + sentence[sentence.rfind('because')+8 : ])
#type 2
print(sentence.replace("because",'').strip())
#type 3
print(" ".join(word for word in sentence.split(" ") if word != "because"))

# bài tập 26
print(sentence.index('because'))

# bài tập 28
sentence ="Coding For All"
print(sentence.startswith('Coding'))

# bài tập 29
print(sentence.endswith("Coding"))
sentence = '   Coding For All      ' 

# bài tập 30
print(sentence.strip())

# bài tập 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# bài tập 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libraries))

# bài tập 33
print("I am enjoying this challenge.{}I just wonder what is next.".format('\n'))

# bài tập 34
print("Name\tAge\tCountry\tCity\n")
print("Asabeneh\t250\tFinland\tHelsinki")

# bài tập 35
f = '''
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
print(f)

# bài tập 36
calculator = '''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
print(calculator)