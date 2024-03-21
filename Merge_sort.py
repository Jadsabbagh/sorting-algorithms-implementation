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

#example:
Array = [27,18,29,9,12,3,32]
sorted_array = divide(Array)
print(sorted_array)