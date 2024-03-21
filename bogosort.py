import random
def Bogosort(original, shuffled):
    while shuffled != original:
        random.shuffle(shuffled)
    return shuffled

#example use:
Sorted_list = [0, 1, 2, 3, 4, 5]
shuffling_list = Sorted_list.copy()
random.shuffle(shuffling_list)

Bogosort(Sorted_list,shuffling_list)
print(shuffling_list)