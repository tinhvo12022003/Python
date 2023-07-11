            #LEVEL 1
#bài tập 1
lst = []

# bài tập 2
lst = [1, 2, 3, 4, 5]

# bài tập 3
print(len(lst))

# bài tập 4
print(lst[0]) #output: 1
print(lst[len(lst) - 1]) #output: 5
print(lst[int((0+len(lst))/2)]) #output: 3

# bài tập 5
mixed_data_types = ['Vo Ngoc Tinh', '20', 170, 'single', 'VietNam']

# bài tập 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# bài tập 7
print(it_companies)

# bài tập 8
print(len(it_companies))

# bài tập 9
print(it_companies[0]) #output: Facebook
print(it_companies[-1]) #output: Amazon
print(it_companies[int((0 + len(it_companies))/2)]) #output: Apple

# bài tập 10
it_companies[0] = "FireFox"
print(it_companies)

# bài tập 11
it_companies.append("Twitter")
print(it_companies)

# bài tập 12 
it_companies.insert(int((0 + len(it_companies))/2), "Samsung")
print(it_companies)

# bài tập 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

# bài tập 14
print("#; ".join(it_companies))

# bài tập 15
print("Google" in it_companies)

# bài tập 16
#type 1
print(sorted(it_companies))
#type 2
it_companies.sort()
print(it_companies)

# bài tập 17
#type 1
it_companies.sort(reverse=True)
print(it_companies)
#type 2
it_companies.reverse()
print(it_companies)

# bài tập 18
first_companies = it_companies[0:4]
print(first_companies)

# bài tập 19
last_companies =  it_companies[-1:-4]
print(last_companies)

# bài tập 20
middle_company = it_companies[int((0 + len(it_companies))/2)]
print(middle_company)

# bài tập 21
del it_companies[0]
print(it_companies)

# bài tập 22
del it_companies[int((0 + len(it_companies))/2)]

# bài tập 23
it_companies.pop()
print(it_companies)

# bài tập 24
it_companies.clear()
print(it_companies)

# bài tập 25
del it_companies


# bài tập 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#type 1
print(front_end + back_end)
#type 2
front_end.extend(back_end)
print(front_end)

# bài tập 27
full_stack = front_end.copy()
print(full_stack)
full_stack.insert(5, "Python")
full_stack.insert(5, "SQL")
print(full_stack)

                #LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
max_age = max(ages)
#print(max_age)
min_age = min(ages)
#print(min_age)

ages.append(min_age); ages.append(max_age)

#print medium age
import math
print(ages[int((0+len(ages))/2)]) if(len(ages) % 2 != 0) else print((ages[math.ceil((0+len(ages))/2)] + ages[math.floor((0+len(ages))/2)])/2)

#print avg age
avg = sum(ages)/len(ages)
print(avg)

#find the range of the ages
print("The range of ages is: {}".format(max_age - min_age))

#Compare the value of (min - average) and (max - average), use abs() method
if (min_age - avg) > (max_age - avg):
    print("(min - average) and (max - average)")
elif (min_age - avg) < (max_age - avg):
    print("(min_age - avg) < (max_age - avg)")
else: print("(min_age - avg) = (max_age - avg)")


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
#Find the middle country(ies) in the countries list
print(countries[int(len(countries)/2)])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
mid = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[0: mid+1]
    last_half = countries[mid+1:]
else:
    first_half = countries[0: mid+1]
    last_half = countries[mid+1:]

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries1, countries2, countries3, *scandic_countries = countries
print(countries1, countries2, countries3, scandic_countries)

