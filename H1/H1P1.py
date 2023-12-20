# Mel Avina-Beltran
# ECS 32B H1 P1 4/11/23
# Sphere: takes the radius of a sphere (a floating-point number) as input and outputs the sphere’s diameter, 
#         circumference, surface area, and volume

def getRad(r):

    # change input from string to float
    r= float(r)

    # add value of pi, so as not to import math
    pi = 3.14

    # forumlas
    diam = 2*r 
    circum = 2*pi*r
    surfaceArea= pi*r*r
    volume = 4/3*pi*r*r*r

    # print and return vars
    print(r, diam, circum, surfaceArea, volume)
    return r, diam, circum, surfaceArea, volume
    
getRad(r)