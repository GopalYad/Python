

#Practising lists

#creating list

list = ["Apple", "banana","papaya", 10, 12 , 2.005,'a','b',True,False]
print(list)

#accessing lists
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
print(list[8])
print(list[9])
# print(list[10])  #index out of range


print("negtive indexing are:\n")
#negative indexing
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])
print(list[-6])
print(list[-7])
print(list[-8])
print(list[-9])
print(list[-10])



#slicing method : range of index : from start to end index
print(list[0:5])
print(list[-9:-1])



#checking if items exist or not 

cList = ["Apple ", "Banana","watermelon"]
if "Apple" in cList:
    print("HA Bhai isme hain")





#change list in items
item = ["maggi","biscut","parle","toffe","egg","fish"]
item[0] = "yeppi"
print(item)

#change by range of index
item[0:3] = ["maggi" , "biscit","candy"]
print(item)



#insert() method used in lists
myList = ["cricket","badminton","football","baseball"]
myList.insert(1,"gilli danda")
print(myList)


#append() method used to add item in the end of list
weeks = ["sunday","monday","tuesday"]
weeks.append("wednesday")
weeks.append("thursday")
weeks.append("friday")
weeks.append("sarturday")
weeks.append("sunday")
print(weeks)

#extend() method used to add list one to another
yourList = ["banana","orange","apple"]
myList = ["mango","watermelon"]
myList.extend(yourList)
print(myList)




#remove() method used to remove element
element = ["Ram","Shyam","sita","RIya"]
element.remove("RIya")
print(element)

#pop() method used to remove items
item = [1,2,23,5,6,65]
item.pop(4)
print(item)

#del keyword ->
del item[0]
print(item)

#clear() method to clear entire items
item.clear()
print(item)



#loop in list --->> for in loop
list_fruit = ["apple","banana","orange"]
for x in list_fruit:
    print(x)

#loop using index numbers
num = [1,2,3,4,5,6,7]
for i in range(len(num)):
    print(num[i])


#loop using while loop
thisList = [12,23 , 34,32,12,5555,23]
i = 0
while i < len(thisList):
    print(thisList[i])
    i=i+1 


#list print in another list
myFavList = ["toy","table ","cherry"]
[print(x) for x in myFavList]