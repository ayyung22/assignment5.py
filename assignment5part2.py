#------------------------
#CIS 103XY Assignment 5
#Your Instructor's Name: Md Ali
#Your Name: Annie Yung
#Date: 10/8/2024

import time
import random

print ("Problem 2: Bubble Sort")

#defining bubble sort function
def bubble_sort(arr):

    for n in range(len(arr) - 1, 0, -1):

        for i in range(n):
            if arr[i] > arr[i + 1]:

                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Created a sample list to be sorted
arr = [2, 4, 9, 15, 3, 17, 100]
print("The unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)

print()
print()


print("Problem 2: Merge Sort")
#defining merge sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
    else:
        sorted_array.append(right[right_index])
        right_index += 1

        sorted_array.extend(left[left_index:])
        sorted_array.extend(right[right_index:])

    return sorted_array

unsorted_array = [2, 4, 6, 8, 10, 12, 14]
sorted_array = merge_sort(unsorted_array)
print("Sorted array:", sorted_array)

print()
print()

print("Problem 2: Comparing Time Complexity")
# Bubble Sort Implementation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

        return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
            sorted_array.extend(left[left_index:])
            sorted_array.extend(right[right_index:])

        return sorted_array

def test_algorithms(sizes):
        for size in sizes:
            data = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.time()
        bubble_sort(data.copy())
        bubble_time = time.time() - start_time
        start_time = time.time()
        merge_sort(data.copy())
        merge_time = time.time() - start_time

print(f"size: {size}")
print(f" Bubble Sort Time: {bubble_sort:.5f} seconds")
print(f"Merge Sort Time: {merge_sort:.5f} seconds")

sizes_to_test = [1000, 10000, 100000]
test_algorithms(sizes_to_test)
