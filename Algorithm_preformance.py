import time
import random
import matplotlib.pyplot as plt
original_array = [i for i in range(5000)] #recommended between 5000 and 10000
arr = original_array.copy()
def Average(lst): 
    return sum(lst) / len(lst) 
from Bubble_sort import bubble_sort
from Insertion_sort import insertion_sort
from Merge_sort import divide, conquer
from Quick_sort import quicksort
from Selection_sort import selection_sort
#bogosort is too inefficient to include :)
if __name__ == '__main__':
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
