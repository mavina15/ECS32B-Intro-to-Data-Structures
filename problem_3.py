# Mel Avina-Beltran
# ECS 32B H1 P3 4/11/23
# Leibniz Forumula: method to approximate the value of π. Program should allow the user to specify the 
#                   number of iterations used in this approximation and displays the resulting value.


def get_pi(n):
    
    # turn string into int
    n = int(n)
    
    # initialize value of pi sum
    totalSum = 0
    
    # for loop: input number of iternations, term is added using summation, output sum of previous iterations and sum of current iteration
    for i in range (n):
        term = (-1)**i/(2*i+1)
        totalSum = totalSum + term
    
    # value of pi sum multiplied by 4
    totalSum = totalSum*4
    
    # print and return value of pi sum
    print(totalSum)
    return totalSum
    
get_pi(n)
