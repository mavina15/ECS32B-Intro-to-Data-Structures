# Mel Avina-Beltran
# ECS 32B H1 P3 1/20/23
# Leibniz Forumula: method to approximate the value of π. Program should allow the user to specify the 
#                   number of iterations used in this approximation and displays the resulting value.

import math

def get_pi(terms):                                      

    sum1 = 0
    
    for i in range(terms):                          # recursive statement for # of terms in series
        sum1 = sum1 + (-1)**i / (2*i + 1)           # formula = sum1 + (-1)^i / (2i + 1)
    sum2 = sum1*4                                   # multiply by 4

    return sum2
