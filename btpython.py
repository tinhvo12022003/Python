#bài tập 1
import string
import math
#a = int(input("nhập số nguyên: "))
#print('YES') if str(a)[len(str(a))-1] == '7' else print('NO')

#bài tập 2
# x, y, z = int(input("Tọa độ x:")), int(input("Tọa độ y:")), int(input("Tọa độ z:"))
# print(abs(x - min(y, z)))

#bài tập 3
# arr = [2, 5, 8, 10, 12]
# print(sum(arr))

#bài tập 4
# import random
# a = random.randint(1, 15)
# guess = int(input("nhap so nguyen: "))
# while(guess != a):
#     if guess > a:
#         print("so nho hon")
#     else:
#         print("so lon hon")
#     guess = int(input("nhap so nguyen: "))

#bài tập 5
# sl = int(input()) * 100
# if sl > 10000:
#     print(sl - sl*10/100)
# else: 
    # print(sl)

#bài tập 6
# arr = [2, 5, 8, 10, 12]
# print([x for x in arr if x % 2 == 0])

#bài tập 7
# arr = [2, 5, 8, 15, 12]
# max = arr[0]
# for x in arr:
#     if x > max:
#         max = x
# print(max)


#bài tập 8
# arr = [5, 2, 8, 3, 10, 6, 18]
# lst = []
# for i in range(1, len(arr)):
#     if arr[i] >= arr[i-1]:
#         lst.append(arr[i])
# print(lst)

#bài tập 9
# arr = [1, 3, 5, 6, 3, 5, 6, 1]
# dif = []
# for x in arr:
#     if x not in dif:
#         dif.append(x)
# print(dif)


#bài tập 10
# arr = [86,86,85,85,85,83,23,45,84,1,2,0] 
# dif = []
# for i in range(len(arr)):
#     if arr[i] not in dif:
#         dif.append(arr[i])
# print(sorted(dif, reverse=True)[:2])

#bài tập 11
# diff = lambda arr: max(arr) - min(arr)
# print(diff([10, 3, 5, 6]))

#bài tập 12
# print([x for x in range(100, 1001) if x % 7 == 0 and x % 5 != 0])

#bài tập 13
# n = int(input())
# def is_prime(x):
#     if x <= 1:
#         return False
#     elif x == 2: return True
#     else:
#         for i in range(2, x):
#             if x % i == 0: return False
#     return True
# print([x for x in range(2, n+1) if is_prime(x)])

#bài tập 14
# arr = [5, 10, 15, 20, 25, 46]
# print("max is {}, min is {}".format(arr[len(arr)-1], arr[0]))

#bài tập 15
# radius = float(input())
# print("Circumference is {}, Area is {}".format(2 * math.pi * radius, math.pi * radius ** 2))



#bài tập 16
# password = input("new password: ")
# confirm_password = input("confirm password: ")
# while password != confirm_password:
#     confirm_password = input("password: ")
# print("password is correct")

#bài tập 17
# n = int(input())
# n_str = str(n)
# sum = 0
# for i in n_str:
#     sum += int(i)
# print(sum)

#bài tập 18
# class App():
#     def __init__(self, param):
#         self.param = param
#     def C_to_F(self):
#         return self.param * 9/5 + 32
    
#     def F_to_C(self):
#         return (self.param - 32) * 5/9
    
#     def kg_to_lb(self):
#         return self.param * 2.20462
    
#     def lb_to_kg(self):
#         return self.param / 2.20462
    
#     def met_to_feet(self):
#         return self.param * 3.28084
    
#     def feet_to_met(self):
#         return self.param / 3.28084

# while(True):
#     print("1. Convert Celsius to Fahrenheit")
#     print("2. Convert Fahrenheit to Celsius")
#     print("3. Convert Kilograms to Pounds")
#     print("4. Convert Pounds to Kilograms")
#     print("5. Convert Metre to Feet")
#     print("6. Convert Feet to Metre")
#     print("7. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         param = float(input("Enter your parameter: "))
#         app = App(param)
#         print(app.C_to_F())
#     elif choice == 2:
#         param = float(input("Enter your parameter: "))
#         app = App(param)
#         print(app.F_to_C())
#     elif choice == 3:
#         param = float(input("Enter your parameter: "))
#         app = App(param)
#         print(app.kg_to_lb())
#     elif choice == 4:
#         param = float(input("Enter your parameter: "))
#         app = App(param)
#         print(app.lb_to_kg())
#     elif choice == 5:
#         param = float(input("Enter your parameter: "))
#         app = App(param)
#         print(app.met_to_feet())
#     elif choice == 6:
#         param = float(input("Enter your parameter: "))
#         app = App(param)
#         print(app.feet_to_met())
#     elif choice == 7:
#         break
#     else:
#         print("Invalid choice")

#bài tập 22
# import numpy as np
# arr = np.random.randint(0, 100, size=10)
# print(arr)
# index = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         index = i
#         break

# print(index)

#bài tập 23
# year = int(input("Year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")

# n = int(input("Enter number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += 1/i
# print(sum)

#bài tập 24
# n = int(input("Enter a number: "))
# print(sum([1/x for x in range(1, n+1)]))

#bài tập 25
# n = int(input("Enter number: "))
# print([x for x in range(1, n+1) if n % x == 0])

#bài tập 26

# def prime_factorize(n):
#     factors = []
#     p = 2

#     while p * p <= n:
#         if n % p == 0:
#             factors.append(p)
#             n //= p
#         else:
#             p += 1

#     if n > 1:
#         factors.append(n)

#     return factors

# number = int(input("Enter a positive integer: "))
# factors = prime_factorize(number)

# print("Prime factors of", number, "are:", factors)

#bài tập 27
# def missing_char(s, n):
#     return s[:n] + s[n+1:]

# print(missing_char('kitten', 0))

#bài tập 28
# def front_back(s):
#     return s[-1] + s[1:-1] + s[0]

# print(front_back('code'))

#bài tập 29
# def caught_speeding(speed, birthday):
#     if birthday == True:
#         speed -= 5
#     return 0 if speed <= 60 and speed >= 0 else 1 if speed >= 61 and speed <= 80 else 2 

# print(caught_speeding(60, True))
# print(caught_speeding(65, False))
# print(caught_speeding(65, True))

#bài tập 30
# def lucky_sum(a, b, c):
#     if a == 13:
#         return 0
#     elif b == 13:
#         return a
#     elif c == 13:
#         return a + b
#     else: 
#         return a + b + c

# print(lucky_sum(1, 2, 3) )
# print(lucky_sum(1, 2, 13) )
# print(lucky_sum(1, 13, 3) )


#bài tập 31
# def big_diff(arr):
#     return max(arr) - min(arr)

# print(big_diff([10, 3, 5, 6]))
# print(big_diff([7, 2, 10, 9]))
# print(big_diff([2, 10, 7, 2]))

#bài tập 32
# import numpy as np
# arr = np.random.randint(0, 100, size=10)
# print(arr)
# print([x for x in arr if x % 2 == 0][-1])

#bài tập 33
# def get_vote_count(dict):
#     return dict['upvotes'] - dict['downvotes']

# print(get_vote_count({ "upvotes": 13, "downvotes": 0 }))
 
# print(get_vote_count({ "upvotes": 2, "downvotes": 33 }))
 
# print(get_vote_count({ "upvotes": 132, "downvotes": 132 }))


#bài tập 34
# def Merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#     L = [0] * (n1)
#     R = [0] * (n2)
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#     i = 0
#     j = 0
#     k = l
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# def mergeSort(arr, l, r):
#     if l < r:
#         m = (l+r)//2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         Merge(arr, l, m, r)

# arr = [5, 5, 2, 8, 10, 7, 12]
# mergeSort(arr, 0, len(arr)-1)
# print(arr)

#bài tập 36
# def UCLN(a, b):
#     return a if b == 0 else UCLN(b, a % b)

# print(UCLN(30, 40))


#bài tập 38
# def line_length(a, b):
#     return math.sqrt(math.pow(abs(b[0] - a[0]), 2) + math.pow(abs(b[1] - a[1]), 2))
# print(line_length([15, 7], [22, 11]))
# print(line_length([0, 0], [1, 1]))


#bài tập 39
# def capital_indexes(str):
#     return [i for i in range(len(str)) if str[i].isupper()]

# print(capital_indexes('HeLlO'))

#bài tập 40
# def symmetry_string(str):
#     reversed = str[::-1]
#     if reversed == str:
#         return True
#     else:
#         return False

# print(symmetry_string('helleh'))

#bài tập 41
# n = int(input('Enter a number: '))
# print('True') if n % math.sqrt(n) == 0 else print('False')


#bài tập 42
# n = int(input('Enter a number: '))
# reverse_number = int(''.join(str(n).split())[::-1])
# print('reverse number is {}'.format(reverse_number))

#bài tập 44
# def sort_list_word(*words):
#     return ", ".join(sorted(words))
# print(sort_list_word('bag', 'hello', 'without' ,'world'))

#bài tập 46
import string
# def count_char(str):
#     alpha = 0
#     num = 0
#     for i in str:
#         if i.isalpha():
#             alpha += 1
#         elif i.isdigit():
#             num += 1
#     return alpha, num
# print('alpha: {}, num: {}'.format(*count_char('hello world! 123')))