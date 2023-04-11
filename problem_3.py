# Mel Avina-Beltran
# ECS 32B H1 P3 4/11/23
# Leibniz Forumula: method to approximate the value of π. Program should allow the user to specify the 
#                   number of iterations used in this approximation and displays the resulting value.


def getPi(n):
    
    n = int(n)
    totalSum = 0
    
    for i in range (n):
        term = (-1)**i/(2*i+1)
        totalSum = totalSum + term
    
    totalSum = totalSum*4
    print(totalSum)
    return totalSum
    
getPi(n)
