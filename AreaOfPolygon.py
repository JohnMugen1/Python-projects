from areaModule import recArea,cicArea,cylArea

#take user option
def take_input():
    print("Solve Mathematics\n1.Calculate area of a rectangle.\n2.Calculate area of a circle.\n3.Calculate area of a closed cylinder.")
    option_num = int(input())
    return option_num

#solve the area of given polygon
def getResults(polygon = take_input()):
    if polygon == 1:
        length = float(input("Enter length:"))
        width = float(input("Enter width:"))
        #get area using recArea() function
        result = recArea(length, width)
        print("Area of the rectangle = ", result)
    elif polygon == 2:
        radius = float(input("Enter radius:"))
        #get area of the circle using cicArea function
        result1 = cicArea(radius)
        print("Area of the circle = ", result1)
    elif polygon == 3:
        radius1 = float(input("Enter the radius:"))
        height = float(input("Enter the height:"))
        #get the area of the cylinder using cylArea function
        result2 = cylArea(radius1, height)
        print("Area of the closed cylinder = ", result2)
    else:
        print("Invalid option!!!")

try:
    getResults()
except ValueError:
    print("Wrong data type entry!Kindly retry again!")
except ZeroDivisionError:
    print("Invalid operation!!Can't divide a number by zero")
except AttributeError:
    print("Invalid method used!retry with the correct method")
except TypeError:
    print("Invalid data used to retrieve certain data!,retry with valid value")
except:
    print("A syntax error!!,kindly re-check and retry again!")
