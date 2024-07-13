

# unlike lists , tuple is immutable in nature ,  it can 't modify

a = (1,2,3,4,5)
print(type(a))

#empty tuple
b = ()
print(b) #output : ()

#one element tuple
c = (1,)
print(c) #output:(1,)

tuple = (1,2,4,5,"Town","City","country" , False , True)
print(type(tuple))  #output:<class 'tuple'>

##can we change element of tuple? no
# tuple[0] = 7 error
print(tuple)


#count(): Returns the number of times a specified value appears in the tuple.
t = (1, 2, 3, 2, 2)
print(t.count(2))  # Output: 3


#index(): Searches the tuple for a specified value and returns the position of where it was found.
t = (1, 2, 3, 2, 2)
print(t.index(3))  # Output: 2


#Slicing: You can slice tuples to obtain a subset of elements.
t = (1, 2, 3, 4, 5)
print(t[1:3])  # Output: (2, 3)


#Concatenation: You can concatenate tuples using the + operator.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)


#Repetition: You can repeat the elements in a tuple using the * operator.
t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)


#Membership: You can check if an element exists in a tuple using the in keyword.
t = (1, 2, 3)
print(2 in t)  # Output: True




