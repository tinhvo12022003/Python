            #LEVEL 1
#bài tập 1
tlp = ()

#bài tập 2
tlp = ("Jonh", "Emily", "Michael", "David", "Emma")

#bài tập 3
brothers = ("John", "Brian", "Michael", "David")
sisters = ("Emily", "Jessica", "Emma", "Olivia")
siblings = brothers + sisters
print(siblings)

#bài tập 4
print(len(siblings))

#bài tập 5
#type 1
family_members = siblings + ("Sarah", "O'neil")
print(family_members)


            #LEVEL 2
#bài tập 1
siblings = family_members[:8]
parents = family_members[8:]
print(siblings, parents)

#bài tập 2
fruits = ("apple", "banana", "cherry")
vegetables = ("lettuce", "tomato", "cucumber")
animals = ("dog", "cat", "mouse")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

#bài tập 3
food_stuff_lt = list(food_stuff_tp)

#bài tập 4
mid = len(food_stuff_tp) // 2
if mid % 2 == 0:
    middle_items = food_stuff_tp[mid]

else: middle_items = food_stuff_tp[mid-1: mid+1]
print(middle_items) 

#bài tập 5
first_three_items = food_stuff_lt[:4]
last_three_items = food_stuff_lt[-3:]

#bài tập 6
del food_stuff_tp

#bài tập 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("True") if "Estonia" in nordic_countries else print("False")
print("True") if "Iceland" in nordic_countries else print("False")