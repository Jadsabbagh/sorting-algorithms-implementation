import time
import random
import matplotlib.pyplot as plt
original_array = [i for i in range(5000)] #recommended between 5000 and 10000
arr = original_array.copy()
def Average(lst): 
    return sum(lst) / len(lst) 
def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0] #pivot as index of comp.
        left = [x for x in array[1:] if x <= pivot]
        right = [x for x in array[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right) #sort left and right reclusively
def bubble_sort(array):
    length = len(array)

    for i in range(length):
        swap = False  # flag to track swaps in iteration

        for x in range(length - i - 1):
            if array[x] > array[x + 1]:  # compare elements
                array[x], array[x + 1] = array[x + 1], array[x]
                swap = True

        if not swap:
            break  # exit loop, array already sorted

    return array
def insertion_sort(array):
    for i in range(1, len(array)):
        pointer = array[i]  # store current element
        comp = i - 1  # index of comparison
        while comp >= 0 and pointer < array[comp]:
            array[comp + 1] = array[comp]
            comp -= 1
        array[comp + 1] = pointer
    return array
def divide(array):
    if len(array) == 1:
        return array
    #divide arrays into halves
    Mid = len(array)//2
    Julius = array[:Mid]
    Caesar = array[Mid:]
    #sort both halves
    Julius = divide(Julius)
    Caesar = divide(Caesar)
    #merge sorted halfs
    return conquer(Julius,Caesar)
def conquer(left,right):
    merged = []
    #comparisions and appending
    while len(left) != 0 and len(right) != 0:
        if left[0]>right[0]:
            merged.append(right[0])
            right.remove(right[0])
        else:
            merged.append(left[0])
            left.remove(left[0])
    #append remaining elements
    while len(left) != 0:
        merged.append(left[0])
        left.remove(left[0])
    while len(right) != 0:
        merged.append(right[0])
        right.remove(right[0])
    return merged
def selection_sort(array):
    length = len(array)
    for num in range(length):
        min_location = num  # current index as min element
        # finding index of minimum index of unsorted portion
        for i in range(num + 1, length):
            if array[min_location] > array[i]:
                min_location = i
        array[num], array[min_location] = array[min_location], array[num]  # swap min element with position 0 of unsorted portion
    return array
#bogosort is too inefficient to include :)
quicksort_preformance = []
for i in range (10):
    random.shuffle(arr)
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    quicksort_preformance.append(execution_time)
    print("Quicksort Execution Time:", execution_time, "seconds")
print(f'Quicksort has an avg time of {Average(quicksort_preformance)} seconds!')

insertion_preformance = []
for i in range (10):
    random.shuffle(arr)
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    insertion_preformance.append(execution_time)
    print("Insertion Sort Execution Time:", execution_time, "seconds")
print(f'Insertion Sort has an avg time of {Average(insertion_preformance)} seconds!')

selection_preformance = []
for i in range (10):
    random.shuffle(arr)
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    selection_preformance.append(execution_time)
    print("Selection Sort Execution Time:", execution_time, "seconds")
print(f'Selection Sort has an avg time of {Average(selection_preformance)} seconds!')

bubble_sort_preformance = []
for i in range (10):
    random.shuffle(arr)
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    bubble_sort_preformance.append(execution_time)
    print("Bubble Sort Execution Time:", execution_time, "seconds")
print(f'Bubble Sort has an avg time of {Average(bubble_sort_preformance)} seconds!')

merge_preformance = []
for i in range (10):
    random.shuffle(arr)
    start_time = time.time()
    divide(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    merge_preformance.append(execution_time)
    print("Merge Sort Execution Time:", execution_time, "seconds")
print(f'Merge Sort has an avg time of {Average(merge_preformance)} seconds!')

preformances = [Average(selection_preformance), Average(merge_preformance), Average(bubble_sort_preformance), Average(insertion_preformance), Average(quicksort_preformance)]
#graphing the data
labels = ['Selection Sort', 'Merge Sort', 'Bubble Sort', 'Insertion Sort', 'Quicksort']
colors = ['blue', 'green', 'red', 'purple', 'orange']
heights = preformances
plt.bar(labels, heights, color=colors)
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (sec)')
plt.title('Average Time of Sorting Algorithms')
plt.show()