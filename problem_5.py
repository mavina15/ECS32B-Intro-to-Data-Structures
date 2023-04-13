# Mel Avina-Beltran
# ECS 32B H1 P5 4/13/23
# List Merge: recursion to merge two sorted lists into a merged list which is obviously a bigger list 
#             containing all elements from the two sorted lists.

def mergeSort(a, b):
    
    # changing strings to lists 
    a = list(a)
    b = list(b)

    # first case, checks if list has no elements 
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    # compares first element of each list, then slices lists and starts again  
    if a[0] < b[0]:
        return [a[0]] + mergeSort(a[1:], b)
    else:
        return [b[0]] + mergeSort(a, b[1:])

def merge(a, b):
    # list elements are 
    if len(a) <= 1 and len(b) <= 1:
        return mergeSort(a, b)
    
    # lists are sliced again  
    oneMid = len(a) // 2
    twoMid = len(b) // 2
    
    oneLeft = a[:oneMid]
    oneRight = a[oneMid:]
    
    twoLeft = b[:twoMid]
    twoRight = b[twoMid:]

    sortLeft = merge(oneLeft, twoLeft)
    sortRight = merge(oneRight, twoRight)
    
    print(mergeSort(sortLeft, sortRight))
    return mergeSort(sortLeft, sortRight)
    
merge(a, b)
