#parent class ,superclass, base class
#child class,sub class,derive class

class phone:
    def call(self):
        print("you can call")

    def message (self):
        print("you can message")

class samsung (phone):
    def photo (self):
        print("you can take photo")

s=samsung()
s.message()
s.call()
s.photo()
print(issubclass(phone,samsung))

class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    def area (self):
        print("I am area method of shape class")

class Triangle(shape):
     #area
     def area (self):
        area= 0.5*self.dim1*self.dim2
        print("Area of Triangle : ",area)
class Rectangle(shape):
     #area
     def area (self):
        area= self.dim1*self.dim2
        print("Area of Rectangle : ",area)
t1=Triangle(10,20)
t1.area()
r1=Rectangle(10,20)
r1.area()