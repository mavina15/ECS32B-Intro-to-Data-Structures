# Mel Avina-Beltran
# ECS 32B H1 P2 4/11/23
# Ball Bounce Experiment: standard science experiment is to drop a ball and see how high it bounces. 
#                         Program should let the user enter the initial height of the ball and the number 
#                         of times the ball is allowed to continue bouncing. Output should be the total 
#                         distance traveled by the ball.

def bounce(initalHeight, index, numBounces):    

    # changing strings to float and int
    height = float(initialHeight)
    numBounces = int(numBounces)
    
    # setting up vars
    index = float(index)
    dist = 0

    # for loop: input # of bounces, output dist and height, runs until no bounces left 
    for i in range(bounces):
        dist = dist + height 
        height = height * index 
        dist = dist + height 
     
    # prints and returns distance traveled
    print(dist)
    return dist

bounce(initalHeight, index, numBounces)
