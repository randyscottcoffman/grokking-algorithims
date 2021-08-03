# Selection Sort is great at sorting things from smallest to largest or vice versa.


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort_small(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

def find_largest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

def selection_sort_large(arr):
    new_arr = []
    for i in range(len(arr)):
        largest = find_largest(arr)
        new_arr.append(arr.pop(largest))
    return new_arr

print(selection_sort_large([8,6,5,4,2]))

print(selection_sort_small([8,6,5,4,2]))