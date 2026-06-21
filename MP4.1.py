#Name : Jeremy Von San Juan
#School : FEU TECH
#MACHINE PROBLEM NUMBER : 1


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"{self.width * self.height}"
        
print("Name : Jeremy Von San Juan")
print("School : FEU TECH")
print("MACHINE PROBLEM NUMBER : 1")




width = float(input("enter the width of the rectangle: "))
height = float(input("enter the height of the rectangle: "))

if width <= 0 or height <= 0:
    print ("The number is not a positive integer")
else:
    areaR = Rectangle(width, height)
    print(f"The area of the rectangle is: {areaR.area()}")