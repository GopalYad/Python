import numpy as np

#creating 1d array
arr=np.array(1,2,3,4,5)
print(arr)

#creating 2d array
arr=np.array([[1,2,3],[4,5,6]])

#creating zeros array
zeros=np.zeros((2,3)) #2x3 array of zeros

#creating ones array
ones=np.ones((3,2)) #3x2 array of ones

#creating an empty array
empty = np.empty((2,2))
print(empty)

#array with range of values
arr=np.aranage(0,1,5)  #5 values from 0 to 1 (inclusive)


#array with evenly spaced values
arr=np.linspace(0,1,5) #5 values  from 0 to 1 (inclusive)

#array attribut

#shape

arr = np.array([[1,2,3],[4,5,6]])  
print(arr.shape) # output : (2,3)

#size
print(arr.size) #output : 6

#Data Type
print(arr.dtype) #ouput : int64


#Reshaping arrays
arr=np.array([[1,2,3],[4,5,6]])
reshaped =arr.reshpe((3,2))
print(reshaped)  #output  : [[1,2],[3,4],[5,6]]

#slicing
arr=np.array([1,2,3,4,5])
print(arr[1:4]) #output: [2,3,4]