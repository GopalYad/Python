tuple=("Apple","banana","cherry","oranges")
print(tuple)


#length of tuple
print(len(tuple))


#recognize tuple
print(type(tuple))

#accessing tuple
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])


#accessing tuples with range of index
print(tuple[0:3])



#update tuple by coverting list
x=(0,1,2,3,4,5)
y = list(x)
y[0]=1
print(y)

#covert tuple into list , add items and convert list into tuple
# m =("Apple","manago","orange")
# n=list(m)
# n.append("watermelon")
# m = tuple(n)



#unpacking the tuple
fruits = ("apple", "banana", "cherry","banana")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#loop in tuple
for x in fruits:
    print(x)

    