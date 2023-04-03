a, b, c, d = 10, 3.14, True, "hello"
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'str'>

# Variable names are case-sensitive.
a=4
A='sallu'
print(a,A)
#A will not overwrite a
# Variables are containers for storing data values.

s="salauddin"
S="samim"
print(s)
print(S)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4 #int
x = "sallu" #str
print(x) 
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
def me():
    global y
    y="awesome"

me()
print("python is " + y)

name='jahid'
id="18192103119"
print("new student name is " +name)
print("new student id is " +id)