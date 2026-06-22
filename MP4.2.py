#Name : Jeremy Von San Juan
#School : FEU TECH
#MACHINE PROBLEM NUMBER : 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{3.14 * self.radius ** 2}"
    def perim(self):
        return f"{2 * 3.14 * self.radius}"


print("Name : Jeremy Von San Juan")
print("School : FEU TECH")
print("MACHINE PROBLEM NUMBER : 1")


radius = float(input("enter the radius of the circle: "))
areaC = Circle(radius)
periC = Circle(radius)

if radius <= 0:
    print ("The number is not a positive integer")
elif radius % 1 != 0:
    print ("The number is not a whole number")
else:
    print(f"The area of the circle is: {areaC.area()}")
    print(f"the perimeter of the circle is : {periC.perim()}")


