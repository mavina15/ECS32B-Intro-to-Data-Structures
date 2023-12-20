# Mel Avina-Beltran
# ECS 32B H1 P2 4/11/23
# Ball Bounce Experiment: standard science experiment is to drop a ball and see how high it bounces. 
#                         Program should let the user enter the initial height of the ball and the number 
#                         of times the ball is allowed to continue bouncing. Output should be the total 
#                         distance traveled by the ball.

import math 

def bounce(bHeight, bBounce, bDistance, bIndex, tBDistance):
    #bHeight = input("Enter ball height (ft): ")                             # ball height input
    #bBounce = input("Enter ball bounce (ft): ")                             # ball bounce input
    
    bHeight = float(bHeight)                                                # convert string to float
    bBounce = float(bBounce)                                                # convert string to float
    
    #bDistance = float(bHeight + bBounce)                                    # ball distance equals sum of ball height and ball bounce
    #bIndex = float(bBounce / bHeight)                                       # ball index equals divisor of ball bounce and ball height
    #tBDistance = float(bDistance + bBounce + (bBounce / 2 + bIndex))        # total distance ball traveled formula
    
    for eachPass in range(bBounce):
        bDistance += bHeight
        bHeight *= bBounce
        bDistance += bHeight 

    #print("Ball's total traveled distance (ft): ", tBDistance)
    
    return [bHeight, bBounce, tBDistance]

    