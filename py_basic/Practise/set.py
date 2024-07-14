#sets are unordered , unchangable
set ={1,2,3,4,5}


#accessing set by only loop and in keyword
for x in set:
    print(x)

print(1 in set)



#add() method to add items in set
set.add("orange")
print(set)


#add item one set to another , use update() method
thisSet={6,7,9}
set.update(thisSet)
print(set)

#remove()
set.remove("orange")
print(set)


#pop()-->randowm item pop
set.pop()
print(set)


#join one set to another return new set 
#union()
s1={1,2,3,4,5}
s2={4,5,6}
s3=s1.union(s2)
print(s3)


# | can be used for same result
a={'a','n','m'}
b={'b','c','d'}
c = a|b
print(c)


#intersection()-->keep only dublicates  or for same result , we can use '&'
num1={1,2,3}
num2={1,4,3}
num3=num1.intersection(num2)
print(num3)


#intersection_update() ->>keep change original set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#difference() --> '-'
set3 = set1 - set2
print(set3)


