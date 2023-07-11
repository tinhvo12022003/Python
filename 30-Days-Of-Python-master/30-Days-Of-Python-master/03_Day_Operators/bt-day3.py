#bài tập 4
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = base * height * 0.5
print("The area of the triangle is: {}".format(area))

#bài tập 5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("The perimeter of the triangle is: {}".format((a + b + c)))

#bài tập 6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("The perimeter of the rectangle is: {}".format(2 * (length + width)))

#bài tập 7
radius = float(input("Enter radius: "))
print("The area of the circle is: {}".format(3.14 * radius ** 2))

#bài tập 8
#calculator slope x-intercept, y-intercept
# y = 2x - 2
slope = 2
x_intercept = 2 / slope
y_intercept = -2
print("slope: {}, x-intercept: {}, y-intercept: {}".format(slope, x_intercept, y_intercept))

#bài tập 9
x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
m = (x2 - x1) / (y2 - y1)
print("slope: {}".format(m))

#bài tập 10
print(slope == m)

#bài tập 11
# y = 2^x + 6x + 9
x = int(input("Enter x: "))
print(2 ** x + 6 * x + 9)

#bài tập 12
print("python".len() == "dragon".len())

#bài tập 13
if("on" in "python" and "on" in "dragon"):
    print("True")
else:
    print("False")

#bài tập 14
#I hope this course is not full of jargon
text = "I hope this course is not full of jargon"
if("jargon" in text):
    print("True")
else:
    print("False")

print("True") if("on" not in "python" and "on" not in "dragon") else print("False")

# bài tập 16
len_int = len("python")
print(len_int)
len_float = float(len_int)
len_str = str(len_float)
print(len_str)

# bài tập 17
number = int(input("Enter a number: "))
print("Even") if number % 2 == 0 else print("Odd")

# bài tập 18
#type 1
result = 7 // 3
converted_value = int(2.7)
if result == converted_value:
    print("True")
else:
    print("False")
#type 2
print(7 // 3 == int(2.7))   #true 

# bài tập 19
#type 1
print("True") if type('10') is type(10) else print("False")
#type 2
print(type(10) is type('10')) #false

# bài tập 20
print(10 == int(9.8)) #false int(9.8) = 9

# bài tập 21
hours, rate_per_hour = int(input("Enter hours: ")), int(input("Enter rate per hour: "))
print("Your weekly earning is {}".format(hours * rate_per_hour))

# bài tập 22
year = int(input())
print("You have live for {} seconds".format(year * 365 * 3600 * 24))

# bài tập 23
import math
for i in range(1, 6):
    print(i, end=" ")
    for j in range(0, 4):
        print(math.pow(i,j), end=" ")
    print(end="\n")
