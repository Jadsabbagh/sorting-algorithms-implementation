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

# Example usage:
if __name__ == '__main__':
    Target_list = [28, 38, 2, 18, 29, 20, 19, 39, 92]
    sorted_array = selection_sort(Target_list)
    print(f'Sorted array: {sorted_array}')
