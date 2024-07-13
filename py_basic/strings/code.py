#string in python

name = "GOPAL"
#access an element
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

#modify -->not possible becausee string is immutable that means you can't modify.
# name[0] = 'T'
# print(name)



                 # String Slicing
#print nickname 
#starts from index 0  all the way till 2 (excluding)
# nickName = name[0:2]
print(name[1:3])
print(name[ : 3])
print(name[0:])
# print(nickName)


a = "0123456789"
print(a[1:7:3])