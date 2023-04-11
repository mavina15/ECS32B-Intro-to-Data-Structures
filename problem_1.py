# Mel Avina-Beltran
# ECS 32B H1 P1 4/11/23
# Sphere: takes the radius of a sphere (a floating-point number) as input and outputs the sphere’s diameter, 
#         circumference, surface area, and volume

def sphere(radius):

    # change input from string to float
    radius = float(radius)

    # add value of pi, so as not to import math
    pi = 3.14

    # forumlas
    diam = 2*radius 
    circum = 2*pi*radius
    surfaceArea= pi*radius*radius
    volume = 4/3*pi*radius*radius*radius

    # print and return vars
    print(radius, diam, circum, surfaceArea, volume)
    return radius, diam, circum, surfaceArea, volume
    
sphere(radius)