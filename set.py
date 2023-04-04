# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

fruitsset = {"apple", "banana", "cherry"}
fruitsset.remove("banana")
print(fruitsset)

num1 = {1,2,3,4,5,6}
num2 =set({6,7,8,9,10})
print (num1 | num2)
print (num1 & num2)