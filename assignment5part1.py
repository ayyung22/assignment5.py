#------------------------
#CIS 103XY Assignment 5
#Your Instructor's Name: Md Ali
#Your Name: Annie Yung
#Date: 10/8/2024

import time
import random


#linear search
print ("Problem 1: Linear Search")
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

#sample array for linear search
arr = [1, 2, 3, 4, 5, 6, 7]
target = 3
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")

print()
print()

print("Problem 1: Binary Search")
#defining function for binary search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

            return -1

sorted_array = [20, 21, 22, 23, 24, 25]
target_value = 24
result = binary_search(sorted_array, target_value)
if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found.")

print()
print()

print("Problem 1: Comparing Time Complexity")
def linear_search(lst,target):
    for index, value in enumerate(lst):
        if value == target:
            return index
        return -1

def binary_search(lst, target):
    left, right = 0, len(lst) -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid -1
            return -1


#creating a function to measure the search times
def measure_search_times(size, target):
    lst = sorted(random.sample(range(size * 10), size))
    start_time = time.time()
    linear_search(lst, target)
    linear_time = time.time() - start_time
    start_time = time.time()
    binary_search(lst, target)
    binary_time = time.time() - start_time
    return linear_time, binary_time

def main():
    sizes = [1000, 10000, 100000]
    target = random.randint(0, 1000000)
    for size in sizes:

        linear_time, binary_time = measure_search_times(size, target)
    print(f"List Size: {size}")
    print(f"Linear Search Time: {linear_time:.6f} seconds")
    print(f"Binary Search Time: {binary_time:.6f} seconds")
    print()

if __name__ == "__main__":
    main()

