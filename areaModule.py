from math import pi,pow
"""areaModule.py - This modules contains area function solutions for various polygons"""
#area of a rectangle
def recArea(length, width):
    return length * width

#area of a circle
def cicArea(radius):
    return pi * radius * radius

#area of a closed cylinder
def cylArea(radius, height):
    return (2 * pi * radius * radius) + (2 * pi * radius * height)

#when this file is run alone
if __name__ == "__main__":
    print("I prefer to be a module, but i can assist you to do some tests.")
    length = 2
    width = 4
    radius = 8
    height = 1
    print(recArea(length, width) == 8)
    print(cicArea(radius) == 201.06192982974676)
    print(cylArea(radius, height) == 452.3893421169302)
    