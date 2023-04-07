import mymodule
mymodule.greeting("samim bai")

import mymodule

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform
x= platform.system()
print (x.upper())

import platform
x=dir(platform)
print(x)

from mymodule import person1
print(person1["age"])