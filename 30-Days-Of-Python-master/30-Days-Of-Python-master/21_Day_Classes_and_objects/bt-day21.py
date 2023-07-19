            #LEVEL 1
#bài tập 1
import statistics as s
import numpy as np
import math

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

mean_ages = s.mean(ages)
median_ages = s.median(ages)
mode_ages = s.mode(ages)

class Statistics():
    def __init__(self, arr):
        self.arr = arr
    
    def mean(self):
        return sum(self.arr) / len(self.arr)

    def median(self):
        sorted_numbers = sorted(self.arr)
        count = len(sorted_numbers)
        middle_index = count // 2
        if count % 2 == 0:
            median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
        else:
            median = sorted_numbers[middle_index]
        return median
    
    def mode(self):
        frequency = {}
        for num in self.arr:
            frequency[num] = frequency.get(num, 0) + 1
        max_frequency = max(frequency.values())
        mode = [num for num, freq in frequency.items() if freq == max_frequency]
        return mode
    

class PersonAccount():
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def account_info(self):
        print(f'First name: {self.firstname}')
        print(f'Last name: {self.lastname}')
        print(f'Income: {self.incomes}')
        print(f'Expense: {self.expenses}')
    
    def add_income(self, income):
        self.incomes += income

    def add_expense(self, expense):
        self.expenses += expense

    def calculate_balance(self):
        return self.incomes - self.expenses


    
