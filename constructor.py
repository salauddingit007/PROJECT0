class student:
    roll=""
    gpa=""

    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"roll :{self.roll},GPA:{self.gpa}")

rahim = student(101,3.75)
rahim.display()

karim = student(102,3.75)
karim.display()

class Triangle:
    def __init__(self,base,height):
        self.base =base
        self.height = height

    def calculate_area(self):
        area=0.5*self.base*self.height
        print ("Area=",area)
t1=Triangle(10,20)
t1.calculate_area()
t2 = Triangle(20,30)
t2.calculate_area()