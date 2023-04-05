class A:
    def display (self):
      print ("i am in A class")

class B:
   def display(self):
      print ("i am in B class")

class C(B,A):
   pass
#    def display (self):
#       print ("i am in C class")

ob1=C()
ob1.display()
