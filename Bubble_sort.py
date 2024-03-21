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

# Example usage:
Target_list = [28, 38, 2, 18, 29, 20, 19, 39, 92]
sorted_list = bubble_sort(Target_list)
print(sorted_list)