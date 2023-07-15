#bài tập 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([num for num in numbers if num <= 0])

#bài tập 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst = [k for i in list_of_lists for j in i for k in j]

#bài tập 3
lst = [(x, x**0, x**1, x**2, x**3, x**4, x**5) for x in range(11) ]

#bài tập 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]

#bài tập 5
countries_dict = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(countries_dict)

#bài tập 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_lst = [first_name +" "+ last_name for [(first_name, last_name)] in names]

#bài tập 7
solve = lambda a, b: "slope is {}, y-intercept is {}".format(a, -b/a)
    


