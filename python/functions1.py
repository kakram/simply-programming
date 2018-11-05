def area(x,y):
    return x * y

def minarea(height=1, width=1):
    return height * width

myarea = area(5,6)

minarea = minarea(width=6, height=8)

print("Area: %s" %myarea)
print("Min Area: %s" %minarea)

