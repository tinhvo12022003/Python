#bài tập 1
#print(", ".join([str(x) for x in range(2000, 3201) if x%7==0 and x%5!=0])) #join với mảng chuỗi


#bài tập 2
# def gt(number):
#     if number < 0: return False
#     if number == 0 or number == 1: return 1
#     return number * gt(number - 1)
# print(gt(8))


#bài tập 3
# n = int(input("Enter a number: "))
# dict = {i : i*i for i in range(1, n+1)} 
# print(dict)


#bài tập 4
# input_str = input("Enter number: ")
# print(list(map(int, input_str.split(','))))
# print(tuple(map(int, input_str.split(','))))


#bài tập 5
# class InputOutString():
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input("Enter a string: ")

#     def printString(self):
#         print(self.s.upper())
# strObj = InputOutString() 
# strObj.getString() 
# strObj.printString()

#bài tập 6
# def square(n):
#     return n**2
# n = int(input("Enter a number: "))
# print(square(n))

#bài tập 7
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def square(n):
#     '''Input square number'''
#     return n**2
# print(square.__doc__)


#bài tập 8
# class Person():
#     name = 'Person'
#     def __init__(self, name=None):
#         self.name = name

# jeffrey = Person("Jeffrey") 
# print ("%s name is %s" % (Person.name, jeffrey.name))  
# nico = Person() 
# nico.name = "Nico" 
# print ("%s name is %s" % (Person.name, nico.name))



#bài tập 9
# import math
# C = 50
# H = 30
# D = input("Enter numbers: ")
# Q = [math.sqrt((2 * C * int(i))/H) for i in D.split(',')]
# print(Q)

#bài tập 10
# n = int(input("Enter rows: "))
# m = int(input("Enter columns: "))
# matrix = [[i * j for j in range(m)] for i in range(n)]
# print(matrix)

#bài tập 11
# string = input("Enter a string: ")
# lst = sorted(string.split(","))
# print(",".join(lst))

#bài tập 12
# lines = [] 
# while True: 
#    s = input() 
#    if s: 
#       lines.append(s.upper()) 
#    else: 
#       break
# for sentence in lines: 
#     print (sentence)

#bài tập 13
# string = input()
# string_set = set(string.split(" "))
# print(" ".join(sorted(list(string_set))))

#bài tập 14
# binary_lst = [x for x in input().split(", ")]
# decimal = {x : int(x, 2) for x in binary_lst if int(x, 2) % 5 == 0}
# print(", ".join(list(decimal.keys())))

#bài tập 15
#print(", ".join(str(i) for i in range(1000, 3001) if all(int(digit) % 2 == 0 for digit in str(i))))


#bài tập 16
# c_count = 0
# d_count = 0
# string = input("")
# for i in string:
#     if i.isdigit():
#         d_count += 1
#     elif i.isalpha():
#         c_count += 1
# print("characters: {}, digits: {}".format(c_count, d_count))


#bài tập 17
# string = input("")
# uppercase = 0
# lowercase = 0
# for i in string:
#     if i.isupper():
#         uppercase += 1
#     elif i.islower():
#         lowercase += 1
# print("uppercase: {}, lowercase: {}".format(uppercase, lowercase))

#bài tập 18
# a = input("Enter a: ")
# n1 = int("%s" %a)
# n2 = int("%s%s" %(a, a))
# n3 = int("%s%s%s" %(a, a, a))
# n4 = int("%s%s%s%s" %(a, a, a, a))
# print(n1 + n2 + n3 + n4)

#bài tập 19
# string = [x for x in input().split(",") if int(x) % 2 != 0]
# print(",".join(str(x) for x in string))
#print(",".join(x for x in input().split(",") if int(x) % 2 != 0))

#bài tập 20
# account = 0
# while True:
#     s = input().split(" ")
#     if s == ['']:
#         break
#     if s[0] == 'D':
#         account += int(s[1])
#     elif s[0] == 'W':
#         account -= int(s[1])
# print(account)

#bài tập 21
# import re
# value = []
# items = [x for x in input().split(', ')]
# pattern =  r"^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@]).{6,12}$"
# for i in items:
#     if re.match(pattern, i):
#         value.append(i)
# print(",".join(value))

# bài tập 22
# from operator import itemgetter, attrgetter
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(',')))
# print(sorted(l, key=itemgetter(0, 1, 2)))

#bài tập 23
# def putNumbers(n):
#     i = 0
#     while i < n:
#         if i % 7 == 0:
#             yield i
#         i += 1
# for i in putNumbers(100):
#     print(i)


#bài tập 24
# import math
# location = [0, 0]
# while True:
#     s = input().split(" ")
#     if s == [""]: break
#     if s[0] == "UP":
#         location[1] += int(s[1])
#     elif s[0] == "DOWN":
#         location[1] -= int(s[1])
#     elif s[0] == "LEFT":
#         location[0] -= int(s[1])
#     elif s[0] == "RIGHT":
#         location[0] += int(s[1])
#     else: pass
# print(round(math.sqrt(pow(location[0], 2) + pow(location[1], 2)), 2))

#bài tập 25
# sentence = input().split(" ")
# words_dict = {}
# for word in sentence: 
#     if word in words_dict: 
#         words_dict[word] += 1
#     else: 
#         words_dict[word] = 1
# print(sorted(words_dict.items()))    

#bài tập 26
# def sum2Numbers(a, b):
#     return a + b
# print(sum2Numbers(1, 2))

#bài tập 27
# def int_to_str(number):
#     return str(number)

# print(int_to_str(123))


#bài tập 28
# def sumnumber(a, b):
#     return int(a) + int(b)


#bài tập 29

# def concat(a, b):
#     return a + b


#bài tập 30
# def printString(a, b):
#     print(a) if len(a) > len(b) else print(b) if len(a) < len(b) else print(a, b)

# printString("Hello", "World")

#bài tập 31
# def checkNumber(a):
#     print("Number is even") if a % 2==0 else print("Number is odd")

# checkNumber(2)


#bài tập 32
# def printDict():
#     print({key:key**2 for key in range(1, 4)})



#bài tập 33
# def printDict():
#     print({key:key**2 for key in range(1, 21)})
# printDict()


#bài tập 34
# def print_ValueDict():
#     print({key:key**2 for key in range(1, 21)}.values())
# print_ValueDict()


#bài tập 35
# def print_KeyDict():
#     print({key:key**2 for key in range(1, 21)}.keys())
# print_KeyDict()


#bài tập 36
# def printList():
#     print([x**2 for x in range(1, 21)])
# printList()

#bài tập 37
# def printList():
#     print([x**2 for x in range(1, 21)][:5])
# printList()


#bài tập 38
# def printList():
#     print([x**2 for x in range(1, 21)][-5:])

# printList()

#bài tập 39
# def printList():
#     print([x**2 for x in range(1, 21)][5:])
# printList()

#bài tập 40
# def printTuple():
#     print(tuple([x**2 for x in range(1, 21)]))
# printTuple()

#bài tập 41
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(tp[:5])
# print(tp[5:])


#bài tập 42
# even_tp = tuple(x for x in tp if x % 2 == 0)
# print(even_tp)

#bài tập 44
# text = input()
# print("Yes") if text.lower() == "yes" else print("No") 

#bài tập 45
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x: x % 2 == 0, lst))
# print(even)


#bài tập 46
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x**2, lst)))

#bài tập 47
#filter() + map()
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x ** 2, filter(lambda x: x%2==0, lst))))

#bài tập 48
# even_lst = list(filter(lambda x: x%2==0, range(1, 21)))
# print(even_lst)

#bài tập 49
#print(list(map(lambda x: x ** 2, range(1, 21))))


#bài tập 50
# class Vietnam(object):
#     @staticmethod
#     def printNationality():
#         print("Vietnam")

# #type1
# Vietnam.printNationality()

# #type2
# Vn = Vietnam()
# Vn.printNationality()


#bài tập 51
# class Vietnam(object):
#     def printNationality(self):
#         print("Vietnam")
# class Hanoi(Vietnam):
#     def printCapital(self):
#         print("Hanoi")
# vn = Vietnam()
# hanoi = Hanoi()
# print(hanoi.printCapital())

#bài tập 52
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# circle = Circle(2)
# print(circle.area())


#bài tập 53
# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return (self.width + self.height) * 2

# rectangle = Rectangle(2, 4)
# print(rectangle.area())

# class Shape():
#     def __init__(self):
#         pass
#     def area(self):
#         pass
# class Square(Shape):
#     def __init__(self, side):
#         Shape.__init__(self)
#         self.side = side
#     def area(self):
#         return self.side ** 2

#bài tập 55
# class RuntimeError(Exception):
#     def __init__(self, mismatch):
#         Exception.__init__(self, mismatch)

# try:
#     print("And now, the vocation Guidance Counseller Sketch.")
#     raise RuntimeError("Does not have proper hat")
#     print("This print statement will not be reached.")
# except RuntimeError as e:
#      print ("Vocation problem: {0}".format(e))


#bài tập 56
# def throws():
#     return 5/0
# try: 
#     throws()
# except ZeroDivisionError as z:
#     print(z)
# except Exception as e:
#     print(e)
# finally:
#     print("out")

#bài tập 60

# import re

# input_str = input().split(" ")
# result = re.findall(r'\b\d+\b', ' '.join(input_str))
# print(result)

#bài tập 61
# unicodeString = u"Hello world"
# print(unicodeString)

#bài tập 62
# s = input()
# print(s.encode('utf-8'))

#bài tập 64
#print(sum([i/(i+1) for i in range(1, 6)]))


#bài tập 65
# def sum(n):
#     if n == 0:
#         return 0
#     return 100 + sum(n-1)
# print(sum(4))

#bài tập 66
# def fibonacci(n):
#     if n == 0: 
#         return 0
#     elif n == 1: 
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

#bài tập 67
# n = int(input("Enter number: "))
# print(", ".join([str(fibonacci(i)) for i in range(n)]))


#bài tập 68
# def evenNumber(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0: 
#             yield i
#         i += 1

# n = int(input("Enter number: "))
# print(", ".join(str(i) for i in evenNumber(n)))

#bài tập 69
# def divide(n):
#     i = 0
#     while i <= n:
#         if i % 5 == 0 and i % 7 == 0:
#             yield i
#         i += 1
# n = int(input("Enter number: "))
# lst = list(str(i) for i in divide(n))
# print(", ".join(i for i in lst))

#bài tập 70
# lst = [2, 4, 6, 8]
# for i in lst:
#     assert i % 2 == 0 

#bài tập 71
# expression = input("Enter expression: ")
# print(eval(expression))

#bài tập 72
# lst = [6, 4, 5, 2, 3, 1, 9, 8, 10, 7]
# def binarySearch(lst, target):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = int((l + r)/2)
#         if lst[mid] == target:
#             return True
#         if lst[mid] < target:
#             l = mid + 1
#         if lst[mid] > target:
#             r = mid - 1
#     return False

# print(binarySearch(sorted(lst), 18)) #output is False
# print(binarySearch(sorted(lst), 6))  #output is True


#bài tập 73
# import random
# import numpy as np
# print(random.random()*100)


#bài tập 74
# import random 
# print(random.random()*100-5)

#bài tập 75
import random
#print(random.choice(range(0, 11, 2)))

#bài tập 76
# print(random.choice([x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]))

#bài tập 77
#print(random.sample(range(100, 201), 5))

#bài tập 78
# print(random.sample(range(100, 201, 2), 5))

#bài tập 79
#print([x for x in range(0,1001) if x % 5 == 0 and x % 7 == 0])
#print(list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(0, 1001))))

#bài tập 80
# print(random.randrange(7, 16))

#bài tập 81
# import zlib
# s = "hello world!hello world!hello world!hello world!"
# t = zlib.compress(s.encode("utf-8"))
# print(t)
# print(zlib.decompress(t))

#bài tập 82
# from timeit import Timer
# t = Timer("for i in range(100):1+1")
# print(t.timeit())

#bài tập 83
# from random import shuffle 
# li = [3,6,7,8]  
# shuffle(li) 
# print (li)

#bài tập 84
# for s in ["Anh", "Em"]:
#     for d in ["Chơi", "Yêu"]:
#         for n in ["Bóng đá", "Xếp hình"]:
#             print(s +" "+ d +" "+ n+"\n")

#bài tập 85
#print(list(filter(lambda x: x%2!=0, [5,6,77,45,22,12,24])))

#bài tập 86
#print(list(filter(lambda x: x%5!=0 and x%7!=0, [12,24,35,70,88,120,155])))

#bài tập 87
#lst = [12,24,35,70,88,120,155]
#enumerate duyệt qua ds vói chỉ số và giá trị của nó
#print([x for i, x in enumerate(lst) if i%2!=0])

#bài tập 88
import numpy as np
# arr = np.zeros((3, 5, 8), dtype=int)
# print(arr)

#bài tập 89
# lst = [12,24,35,70,88,120,155]
# print([x for i, x in enumerate(lst) if i not in [0, 4, 5]])

#bài tập 90
# lst = [12,24,35,24,88,120,155]
# print(list(filter(lambda x: x != 24, lst)))

#bài tập 91
# lst1 = set([1,3,6,78,35,55])
# lst2 = set([12,24,35,24,88,120,155])
# print(lst1.intersection(lst2))

#bài tập 92
# lst = set( [12,24,35,24,88,120,155,88,120,155])
# print(list(lst))

#bài tập 93

# class Nguoi():
#     def __init__(self, gender):
#         self.gender = gender
    #   def getGender(self):
    #     return "Unknown"

# class Nam(Nguoi):
#     def getGender(self):
#         return self.gender
# class Nu(Nguoi):
#     def getGender(self):
#         return self.gender
    
# Nam = Nam("Nam")
# print(Nam.getGender())

#bài tập 94
# def count_char(param):
#     count = {}
#     for i in param.split(" "):
#         for j in i:
#             if j in count:
#                 count[j] += 1
#             else:
#                 count[j] = 1
#     return count
# print(count_char("hello world"))

#bài tập 95
# string = input()
# print(string[::-1])

#bài tập 96
# import re
# string = input()
# print(re.sub(r'[^a-zA-Z.]', '', string))


#bài tập 98
# for i in range(36):
#     for j in range(36):
#         if 2*i + 4*j == 94:
#             print(i, j)
        