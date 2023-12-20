# Mel Avina-Beltran
# ECS 32B H1 P6 1/20/23
# List Merge: recursion to merge two sorted lists into a merged list which is obviously a bigger list 
#             containing all elements from the two sorted lists.

def merge(list1,list2):

    list3= []                                           # new list where combined and sorted # will go

    i = 0                                               # counters for list 1, list2
    j = 0

    while i < len(list1) and j < len(list2):            # recursive function checking the length of each list
        if list1[i] <= list2[j]:                        # if the number in list1 is <= number in list2
            list3.append(list1[i])                      # the number in list1 is added to the new list
            i += 1                                      # the counter increases by 1 and then the number in
            continue                                    # list2 is added to the new list then the counter for 
        list3.append(list2[j])                          # list 2 is increased by 1, where the procress repeats
        j += 1                                          # until the lists have no more 

    while i < len(list1):                               # this and bottom recursive function are used in case
        list3.append(list1[i])                          # there are any remaining numbers in either list to
        i = i + 1                                       # to be returned
        
    while j < len(list2):
        list3.append(list2[j])
        j = j + 1
        
    return list3



