#fibonanci
def fibonaci(n):
    if n < 0: return -1
    if n == 0 or n == 1: return 1
    return fibonaci(n-1) + fibonaci(n-2)

# n = int(input())
# for i in range(n):
#     print(fibonaci(i), end=" ")


def isPrame(n):
    if n <= 1: return False
    if n == 2: return True
    if n > 2:
        for i in range(2, n, 1):
            if n % i == 0: return False
    return True


# n = int(input())
# for i in range(n): 
#     if isPrame(i) == True:
#         print(i, end=" ")

def factorial(n):
    if n == 0 or n == 1: return 1
    else: return factorial(n-1) * n


# n = int(input())
# print(factorial(n))

def decimal_to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    digits = digits[::-1]
    return ''.join(str(d) for d in digits)

# n = int(input("Nhap so n: "))
# base = int(input("Nhap so base: "))


# array = []
# for i in range(10, 201):
#     if i % 7 == 0 and i % 5 != 0:
#         array.append(str(i))
# print(', '.join(array))

# def factorial(n):
#     if n == 0: return 1
#     mul = 1
#     while n > 0:
#         mul = mul * n
#         n -= 1
#     return mul

# res = factorial(3)
# print(res)

# def dictionary(n):
#     dict = {}
#     for i in range(1, n+1): dict.update({i: i*i})
#     return dict

# n = int(input())
# print(dictionary(n))

from abc import abstractmethod
import math
import os
def ptbac_2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0: print(f'Phuong trinh vo so nghiem')
            else: print(f'Phuong trinh vo nghiem')
        else: print(f'Phuong trinh co nghiem x = {-c/b}')
    else:
        delta = math.pow(b, 2) - 4 * a *c
        if delta < 0: print(f'Phuong trinh vo nghiem')
        elif delta == 0: print(f'Phuong trinh có nghiem kep: x1 = x2 = {-b/(2*a)}')
        else: print(f'Phuong trinh co 2 nghiem phan biet: x1 = {round((-b + math.sqrt(delta))/(2*a), 2)}, x2 = {round((-b - math.sqrt(delta))/(2*a), 2)}')
    
# ptbac_2(5, 8, 2)

# def isPrame(n):
#     if n <= 1: return False
#     if n == 2: return True
#     if n > 2:
#         for i in range(2, n, 1):
#             if n % i == 0: return False
#     return True

# for i in range(10001, 99999):
#     if isPrame(i) == True:
#         print(str(i) + " ")

# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors


# circle = lambda x, y: (math.pi * math.pow(x, 2))

# try:
#     x = int(input("Nhập một số nguyên: "))
#     y = 1 / x
# except ValueError:
#     print("Giá trị nhập vào không phải là một số nguyên.")
# except ZeroDivisionError:
#     print("Không thể chia một số cho 0.")
# except:
#     print("Một lỗi xảy ra.")
# else:
#     print("Không có lỗi xảy ra.")
# finally:
#     print("Chương trình đã kết thúc.")

# list = [1, 2, 3, 4, 5, 6]
# try:
#     a = list[4]
# except IndexError:
#     print("Không tồn tại")
# else:
#     print(a)
# finally: print("thoát")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __delattr__(self):
#         print("Huy doi tuong")
# person = Person("John", 25)

# # Thiết lập giá trị của thuộc tính "name" của đối tượng "person"
# setattr(person, "name", "Adam")
# print(person.name)  # Output: "Adam"

# # Thiết lập giá trị cho một thuộc tính mới "gender" của đối tượng "person"
# setattr(person, "gender", "male")
# # print(person.gender)  # Output: "male"
# setattr(person, "nation", "England")
# print(person.age, person.name, person.gender, person.nation)
# person.__delattr__(person)
# print(person.age, person.name, person.gender, person.nation)

# import math
# class Shape:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# class square(Shape):
#     def area(self): return self.a * self.b

# class Circle(Shape):
#     def area(self): return math.pi * math.pow(self.a, 2)

# area = Circle(3, 4)
# print(area.area())    


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print("Name:", self.name, "Age:", self.age)
# class Student(Person):
#     @abstractmethod
#     def __init__(self, name, age, id, score):
#         super().__init__(name, age)
#         self.id = id
#         self.score = score
#     @abstractmethod
#     def show(self):
#         print("Name:", self.name, "Age:", self.age, "ID:", self.id, "Score:", self.score)

# class Teacher(Person):
#     @abstractmethod
#     def __init__(self, name, age, salary, object):
#         super().__init__(name, age)
#         self.salary = salary
#         self.object = object
    
#     @abstractmethod
#     def show(self):
#         print("Name:", self.name, "Age:", self.age, "Salary:", self.salary, "Object:", self.object)

# student = Student("Harry", 19, 1, 100)
# student.show()



# class Person:
#     def __init__(self, name, age):
#         self.name = name         # public variable
#         self._age = age          # protected variable
#         self.__id = 1234         # private variable

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self._age}")
#         print(f"ID: {self.__id}")

#     def change_age(self, new_age):
#         self._age = new_age

#     def __change_id(self, new_id):
#         self.__id = new_id

# person = Person("John", 30)

# # Accessing public variable
# print(person.name)

# # Accessing protected variable
# print(person._age)

# # Trying to access private variable throws an AttributeError
# # print(person.__id)

# # Instead, we can access it using name mangling
# print(person._Person__id)

# person.display_info()

# # Changing the protected variable
# person.change_age(40)

# # Trying to call a private method throws an AttributeError
# # person.__change_id(5678)

# # Instead, we can call it using name mangling
# person._Person__change_id(5678)

# person.display_info()

class CD:
    def __init__(self) -> None:
        pass



    def __write_file(self, info_CD, singer_name, song_numbers, price, endcoding = "utf-8"):
        content = open("CD.txt", "a+", encoding=endcoding)
        content.write(f"{info_CD}, {singer_name}, {song_numbers}, {price}\n")
        content.close()



    def __read_file(self):
        content = open("CD.txt", "r+")
        return content.read()



    def input_info(self):
        print("1. Thêm CD: ", end = " " ); info_CD = input()
        print("2. Tên ca sĩ: ", end = ""); singer_name = input()
        print("3. Số bài hát: ", end = " "); song_numbers = input()
        print("4. Giá: ", end = " "); price = input()
        self.__write_file(info_CD, singer_name, song_numbers, price)



    def show(self):
        print("---- Danh sách CD: ---")
        my_info = self.__read_file()
        print(my_info)


        

    def insert_CD(self):
        print("Tiếp tục nhập: 1: Có, 0: Không", end = " ")
        yes = int(input())
        if yes == 0:
            pass
        else: 
            self.input_info()



    def delete_CD(self):
        n = int(input("Nhập số dòng cần xóa: "))
        with open('CD.txt', 'r') as file:
            lines = file.readlines()
# Xóa dòng thứ 3
            del lines[n-1]
        with open('CD.txt', 'w') as file:
            for line in lines:
                file.write(line)


    def CD_menu(self):
        print("-------------------------------")
        print("# 1. Thêm CD                  #")
        print("# 2. Xóa CD                   #")
        print("# 3. In thông tin CD          #")
        print("# 0. Thoát                    #")
        print("# 4. Sắp xếp                  #")
        print("#                             #")
        print("#                             #")
        print("-------------------------------")


    def sum_price(self):
        with open('CD.txt', 'r') as file:
            lines = file.readlines()
        total = 0
        for line in lines:
            info = line.split(', ')
            total += int(info[-1])
        return total
    
# cd1 = CD()
# while(True):
#     cd1.CD_menu()
#     n = int(input("Nhập lựa chọn: "))
#     if n == 1:
#         cd1.input_info()
#     elif n == 2:
#         cd1.delete_CD()
#     elif n == 3:
#         cd1.show()
#     elif n == 4:
#         cd1.sort_CD()
#     elif n == 0:
#         break

# def main(*person):
#     print(type(person))
#     print(person[2])

# main("C", "C++", "Java", "Python", "JavaScript", "C#")

# a = []
# for i in 10:
#     n = int(input())
#     a = a.append(n)
# for i in 10:
#     print(a[i])

# import base64
# message = "Hello, world!"
# message_bytes = message.encode("ascii")
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode("ascii")
# print(base64_message)

# base64_bytes = base64_message.encode("ascii")
# message_bytes = base64.b64decode(base64_bytes)
# message = message_bytes.decode("ascii")
# print(message)

# import matplotlib.pyplot as plt
# import numpy as np
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel = np.poly1d(np.polyfit(x, y, 3.3))
# myline = np.linspace(0, 22, 100)
# plt.plot(myline, mymodel(myline))
# plt.scatter(x, y)
# plt.show()

# import numpy
# from sklearn.metrics import r2_score

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# print(r2_score(y, mymodel(x)))
# from sklearn import linear_model
# import pandas as pd
# df = pd.read_csv("data.csv")
# X = df[['Volume', 'Weight']]
# Y = df['CO2']

# regr = linear_model.LinearRegression()
# regr.fit(X, Y)

# predictCO2 = regr.predict([[3300, 1300]])
# print(predictCO2)
# print(regr.coef_)

# import numpy as np

# arr = np.array([1, 2, 3])
# std = np.mean(arr)

# print(std)
# import numpy
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score 

# a = numpy.random.seed(2)
# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100)/x
# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# plt.scatter(train_x, train_y)

# mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# myline = numpy.linspace(0, 6, 100)

# plt.plot(myline, mymodel(myline))

# # plt.show()
# print(r2_score(test_y, mymodel(test_x)))
# print(mymodel(5))

# import pandas as pd
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt

# df = pd.read_csv("data3.csv")
# d = {'UK' : 0, 'USA' : 1, 'N' : 2}
# df['Nationality'] = df["Nationality"].map(d)

# d = {'YES' : 1, 'NO' : 0}
# df["Go"] = df["Go"].map(d)

# features = ["Age", "Experience", "Rank", "Nationality", "Go"]

# X = df[features]
# Y = df["Go"]

# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, Y)

# tree.plot_tree(dtree, feature_names=features)
# plt.show()

