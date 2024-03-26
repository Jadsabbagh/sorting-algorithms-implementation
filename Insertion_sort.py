def insertion_sort(array):
    for i in range(1, len(array)):
        pointer = array[i]  # store current element
        comp = i - 1  # index of comparison
        while comp >= 0 and pointer < array[comp]:
            array[comp + 1] = array[comp]
            comp -= 1
        array[comp + 1] = pointer
    return array

# Example usage:
if __name__ == '__main__':
    Array = [10, 28, 2810, 37, 1, 182, 17]
    sorted_array = insertion_sort(Array)
    print(f'Sorted array: {sorted_array}')
