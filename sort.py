
import math

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(a):
    n = len(a)
    for i in range(n):
        min_pos = i
        value = a[i]
        while min_pos > 0 and a[min_pos-1] > value:
            a[min_pos] = a[min_pos-1]
            min_pos -= 1
        a[min_pos] = value
    return a

def selection_sort(a):
    n = len(a)
    for i in range(n):
        index_min = i
        for j in range(i+1, n):
            if(a[index_min] > a[j]):
                index_min = j
        if(index_min != i):
            a[index_min], a[i] = a[i], a[index_min]
    return a

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = []
    R = []
    for i in range(n1):
        L[i] = a[l+i]
    for j in range(n2):
        R[j] = a[m+j+1]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]: 
            a[k] = L[i]
            i += 1
            k += 1
        else: 
            a[k] = R[j]
            j += 1
            k += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
def merge_sort(arr):
    # If the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # Add any remaining elements from the left or right half
    merged += left_half[i:]
    merged += right_half[j:]

    return merged

def sheaker_sort(a):
    n = len(a)
    left = 0
    right = n -1 
    while left < right:
        for i in range(left, right):
            if(a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                
        for j in range(right, left):
            if(a[j-1] > a[j]):
                a[j], a[j-1] = a[j-1], a[j]
                
        left += 1
        right -= 1
    return a

def shell_sort(a):
    n = len(a)
    for interval in range(int(n/2), 0, -1):
        for i in range(interval, n):
            tmp = a[i]
            j = i
            while j >= interval and a[j-interval] > tmp:
                a[j] = a[j-interval]
                j -= interval
            a[j] = tmp
    return a


def quick_sort(a, l, r):
    p = a[int((l+r)/2)]
    i = l
    j = r
    if l < r:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        
        if i < r:
            quick_sort(a, i, r)
        
        if l < j:
            quick_sort(a, l, j)
    return a