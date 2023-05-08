import math
 
#CIRCLE
class Circle():
    def _init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius)*(self.radius)
    
radius = float(input("enter the radius of a circle:"))   
circle = Circle(radius)
print("area of a circle is:",circle.area())
#SQUARE
class Square():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return x * y
x = float(input("enter the x value:"))    
y = float(input("enter the y value:"))    
obj = Square(x,y)
print("area of a square is:",obj.area())
#RECTANGLE
class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return a * b
a= float(input("enter the a value:"))    
b = float(input("enter the b value:"))    
obj = Rectangle(a,b)
print("area of a Rectangle is:",obj.area())
#CYLINDER
class Cylinder():
    def __init__(self,rad,height):
        self.rad = rad
        self.height = height
    def vol(self):
        return math.pi * (rad*rad) * height
rad = float(input("enter the radius of a cylinder:")) 
height = float(input("enter the height of cylinder:"))
obj = Cylinder(rad,height)
print("volume of a Cylinder is:",obj.vol())
#TRIANGLE
class Triangle():
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        return 1/2*b*h
b = float(input("enter the bredth:"))
h = float(input("enter the height:"))
tri = Triangle(b,h)
print("area of a triangle:",tri.area())


