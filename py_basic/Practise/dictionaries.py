thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])


print(len(thisdict))


#accessing .[] or get() method
#keys() 
#values()
x= thisdict.keys()
print(x)
y = thisdict.values()
print(y)


#modify 
thisdict["brand"] = "toyata"
print(thisdict)


#modify --> update() method as in dictionary as
thisdict.update({"year":2004})
print(thisdict)


#add item -->updaate
thisdict.update({"color":"red"})
print(thisdict)


#remove pop()
thisdict.pop("brand")
print(thisdict)

#remove del
del thisdict["model"]
print(thisdict)



#loop in dictionaries
for x in thisdict.keys():
    print([x])

    
for x in thisdict.values():
    print([x])

for x , y in thisdict.items():
    print(x,y)


#nested dictionaries
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
#access
print(myfamily["child1"]["name"])  #Emil
print(myfamily["child2"])


#loop through keys and values
for x , y in myfamily.items():
    print(x,y)




# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary