def ballBounce(height, bounces):    

    height = float(height)
    bounces = int(bounces)
    index = 0.6
    dist = 0

    for i in range(bounces):
        dist = dist + height 
        height = height * index 
        dist = dist + height 
        
    print(dist)
    return dist

ballBounce(height,bounces)
