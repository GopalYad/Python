#lists are the container to store  a set of  values of an data types.

list =["Apple", "Orange ",  2 , 3.444 ,  False , "Akash" , "Rohan" ]

print(list[0]) 


#lists are mutable in nature it can be change or modify of an element of list
list[0] = "banana"

print(list[0]) 



#list can be indexed like a strings
print("element at 0 :" , list[0])
print("element at 1 :" , list[1])
print("element at 2 :" , list[2])
print("element at 3 :" , list[3])
print("element at 4 :" , list[4])
print("element at 5 :" , list[5])


#list can be sliced like string
print(list[0:3])
print(list[1:5])
print(list[2:5])
print(list[0:1])
print(list[0:4])


#lists are mutable in nature even if use method it can be modity to make new list
fruit = ["Apple","Banana","pineApple","Grapes"]
print(fruit)
fruit.append("orange")
print(fruit)


#list have many inbuilt methods:

#1) sort() method

n = [10,5,1,2,7,3,1]
n.sort() 
print(n) #output :[1, 1, 2, 3, 5, 7, 10]


#2) reverse() method
n.reverse()
print(n) #output :[10, 7, 5, 3, 2, 1, 1]

#3) insert(index , value)
n.insert(3,3333)
print(n) #output :[10, 7, 5, 3333, 3, 2, 1, 1]

#4) pop(index)
n.pop(3)
print(n)

#5) remove(value)
n.remove(1)
print(n) #output: [10, 7, 5, 3, 2, 1]   