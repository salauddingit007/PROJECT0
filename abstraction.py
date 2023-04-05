# # Python program demonstrate  
# # abstract base class work   
# from abc import ABC, abstractmethod   
# class Car(ABC):   
#     def mileage(self):   
#         pass  
  
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
  
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ")   
          
# # Driver code   
# t= Tesla ()   
# t.mileage()   
  
# r = Renault()   
# r.mileage()   
  
# s = Suzuki()   
# s.mileage()   
# d = Duster()   
# d.mileage()  

from abc import ABC ,abstraction

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
        
@abstraction
def area (self):
      pass

class Triangle(shape):

     def area (self):
        area= 0.5*self.dim1*self.dim2
        print("Area of Triangle : ",area)

class Rectangle(shape):
   
     def area (self):
        area= self.dim1*self.dim2
        print("Area of Rectangle : ",area)

t1=Triangle(10,20)
t1.area()
r1=Rectangle(10,20)
r1.area()

