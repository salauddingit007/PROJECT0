class Myclass:
    x=7
p1 = Myclass()
print(p1.x)

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def _init_(self, name, age):
        self.name  = name
        self.age = age
p1 = Person ("sallu", 23)

print(p1.name)
print(p1.age)\
# The string representation of an object WITHOUT the __str__() function:
# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("sallu", 23)

# print(p1)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
      print("Hello my name is " + self.name)

p1 =  Person("sajib", 24)
p1.myfunc()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print( thisdict["brand"])