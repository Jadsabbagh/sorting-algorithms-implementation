def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0] #pivot as index of comp.
        left = [x for x in array[1:] if x <= pivot]
        right = [x for x in array[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right) #sort left and right reclusively

#example usage:
arr = [473, 37, 18, 10, 1, 75, 1]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
