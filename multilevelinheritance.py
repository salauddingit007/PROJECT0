class A:
    def display1 (self):
      print ("i am in A class")

class B(A):
   def display2 (self):
      print ("i am in B class")

class C(B):
   def display3 (self):
      super().display1()
      super().display2()
      print ("i am in C class")

ob1=C()
ob1.display1()
ob1.display2()
ob1.display3()

   
