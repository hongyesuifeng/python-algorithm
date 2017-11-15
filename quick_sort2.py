"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    less = []
    equal = []
    large = []
    if len(array) > 1:
        pivot = array[0]
        for each in array:
            if each > pivot:
                large.append(each)
            elif each == pivot:
                equal.append(each)
            else:
                less.append(each)
        return quicksort(less) + equal + quicksort(large)
    else:
        return array
            

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))

