        #LEVEL 1
#bài tập 1
age = int(input("Enter your age: "))
print("You are old enough to learn to drive.") if age >= 18 else print("You need {} more years to learn to drive.".format(18 - age))

#bài tập 3
a, b = int(input("Enter number one: ")), int(input("Enter number two: "))

print("{} is {} than {}".format(a, 'greater' if a > b else 'less', b))

            #LEVEL 2
#bài tập 1
scores = int(input('Enter your score: '))
print("{}".format('A' if scores >=80 and scores <=100 else 'B' if scores >=70 and scores < 80 else 'C' if scores >= 60 and scores < 70 else 'D' if scores >= 50 and scores <= 60 else 'F'))

#bài tập 2
month = input("Enter your month: ")
season_dct = {
    'Winter': ['Januaru', 'Febuary', 'December'],
    'Spring': ['March', 'April', 'May'], 
    'Summer': ['June', 'July', 'August'],
    'Autumn': ['September', 'October', 'November']
}
season = ''
for key, values in season_dct.items():
    if month in values:
        season = key
        break
if season:
    print("The season is {}".format(season))
else: 
    print("The season is invalid")

#bài tập 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Input fruit: ")
print("That fruit already exist in the list") if fruit in fruits else fruits.append(fruit) and print(fruits)

                #LEVEL 3
#bài tập 4

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
key = 'skills'
print(person['skills'][int((len(person['skills']))/2)]) if key in person.keys() else print("No skills")

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if key in person.keys():
    if 'Python' in person['skills']:
            print("The person has Python skill")
    else:
            print("The person doesn't have Python skill")
else: print("No skills")


#JavaScript and React -> print('He is a front end developer')
#Node, Python, MongoDB ->  print('He is a backend developer')
#React, Node and MongoDB -> Print('He is a fullstack developer')



print('{} {} lives in {}. He is {}.'.format(person['first_name'], person['last_name'], person['country'], 'married' if person['is_marred'] == True else 'not married'))