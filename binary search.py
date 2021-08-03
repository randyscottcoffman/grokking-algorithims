# binary search requires a sorted array, that then picks the middle number in the array. 
# Once the middle number is chosen, it then keeps checking the middle number until it finds the item or it returns NULL/-1

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        print(guess) #printing guess so people can run it without a debugger to see how it chooses a guess while within the loop
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

array_1 = [i for i in range(500)] 

binary_search(array_1,73)