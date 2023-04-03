# Change the "year" to 2018:
changedict = {
  "brand": "freedom",
  "model": "bangladesh",
  "year": 1971
}
changedict["year"] = 2023
print(changedict["year"])

# Update the "year" of the fight by using the update() method:

updatedict = {
  "brand": "freedom",
  "model": "bangldesh",
  "year": 1971
}
updatedict.update({"year": 1975})
print(updatedict["year"])

# The pop() method removes the item with the specified key name:

removedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
removedict.pop("model")
print(removedict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

popitemdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
popitemdict.popitem()
print(popitemdict)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

for x in thisdict.values():
  print(x)

#   Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# A dictionary can contain dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)