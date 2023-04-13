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
    mid1 = len(a) // 2
    mid2 = len(b) // 2
    
    oneLeft = a[:mid1]
    oneRight = a[mid1:]
    
    twoLeft = b[:mid2]
    twoRight = b[mid2:]

    sortLeft = merge(oneLeft, twoLeft)
    sortRight = merge(oneRight, twoRight)
    
    print(mergeSort(sortLeft, sortRight))
    return mergeSort(sortLeft, sortRight)
    
merge(a, b)
