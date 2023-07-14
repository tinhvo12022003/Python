        #LEVEL 1
#bài tập 1
def add_two_numbers(a, b):
    return a + b

#bài tập 2
import math
def area_of_circle(radius):
    return math.pi * math.pow(radius, 2)

#bài tập 3
def add_all_nums(*nums):
    for i in nums:
        if not isinstance(i, (int, float)):
            return "Invalid"
    return sum(nums)

#bài tập 4
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


#bài tập 5
def check_season(month):
    if month == 12 or month == 1 or month == 2:
        return "Winter"
    elif month == 3 or month == 4 or month == 5:
        return "Spring"
    elif month == 6 or month == 7 or month == 8:
        return "Summer"
    elif month == 9 or month == 10 or month == 11:
        return "Autumn"
    
#bài tập 6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

#bài tập 7
def solve_quadratic_eqn(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

#bài tập 8
def print_list(*lst):
    print([i for i in lst], end=" ")
    print("\n")

#bài tập 9
def reverse_list(lst):
    lst = lst[::-1]
    return lst

#bài tập 10
def capitalize_list_item(*lst):
    return [i.capitalize() for i in lst]

#bài tập 11
def add_item(lst, item):
    new_lst = lst.copy()
    new_lst.append(item)
    return new_lst

#bài tập 12
def remove_item(lst, item):
    new_lst = lst.copy()
    new_lst.remove(item)
    return new_lst

#bài tập 13
def sum_of_number(num):
    return sum(range(1, num + 1))

#bài tập 14
def sum_of_odd(num):
    return sum(range(1, num + 1, 2) if num % 2 != 0 else [])

#bài tập 15
def sum_of_even(num):
    return sum(range(0, num+1, 2))

            #LEVEL 2

#bài tập 1
def evens_and_odds(num):
    return len([i for i in range(0, num + 1) if i % 2 == 0]), len([i for i in range(0, num + 1) if i % 2 != 0])

#bài tập 2
def factorial(num) :
    if num == 0 or num == 1: return 1
    else: return num * factorial(num - 1)

#bài tập 3
def is_empty(param):
    if not param:
        return True
    else:
        return False

#bài tập 4
import numpy as np
def calculate_mean(*lst):
    return np.mean(lst)
def calculate_median(*lst):
    return np.median(lst)
def calculate_mode(*lst):
    return np.mode(lst)
def calculate_range(*lst):
    return np.max(lst) - np.min(lst)
def calculate_variance(*lst):
    return np.var(lst)
def calculate_std(*lst):
    return np.std(lst)

            #LEVEL 3
#bài tập 1
def is_prime(num):
    return len([i for i in range(2, num) if num % i == 0]) == 0

#bài tập 2
def check_unique_list(lst):
    return len(lst) == len(set(lst))

#bài tập 3
def check_data_type(lst):
    if len(set(map(type, lst))) == 1:
        return True
    else:
        return False

#bài tập 4  
import re 
def check_valid_var(var_name):
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var_name):
        return True
    else:
        return False
    




