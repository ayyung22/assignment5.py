#------------------------
#CIS 103XY Assignment 5
#Your Instructor's Name: Md Ali
#Your Name: Annie Yung
#Date: 10/8/2024

import time

print("Problem 4: Analyzing Python's Built-In Sorting Algorithm")
my_list = [1, 2, 3, 4, 5, 6]
sorted_list = sorted(my_list)
print(sorted_list)

print()
print()

print("Problem 4: Measuring the performance of sorted() and merge sort")
#created sorted function and measuring the time complexity
#creating a bigger list
my_list = [1, 2, 3, 4, 5, 6] * 1000
sorted_list = sorted(my_list)
start_time = time.time()
sorted_numbers = sorted(my_list)
end_time = time.time()
print("Time taken to sort:", end_time - start_time, "seconds")

def merge_sort(left, right):
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

#measuring the time complexity of merge sort
#using merge sort
numbers = [1, 2, 3, 4, 5, 6] * 1000
start_time = time.time()
merge_sort(numbers)
end_time = time.time()
print("Time taken to sort using merge sort:", end_time - start_time, "seconds")
print()
print()

print("Problem 4: Why is Timsort more efficient than merge sort")
#Timsort is more efficient than merge sort as it's a hybrid of merge sort and insertion sort. Timsort initially takes insertion sort and sorts out small sub=arrays of data.
#Once the sub-arrays are sorted, it will use merge sort to combine all of the data.