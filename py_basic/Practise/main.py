# Convert a list of integers to floats and compute the average
list =[1,2,3,4,5,6]
#converting list Integer into float
float_value = [float(i)for i in list]
sum_of_list=0
#iterating to get sum of all the element
for num in float_value:
    sum_of_list+=num
#getting average
average=sum_of_list/len(float_value)

#print the average finally
print(f"The average is :{average} ")


#Determine if a given integer is even or odd.
check_even_odd = lambda x : x % 2==0
print(check_even_odd(2))

#Write a function that returns True if a float is positive and False otherwise
def check_postive (n):
    if(n>0):return True
    else : return False 
   
print(check_postive(-2))

#Write a function that finds the maximum of three numbers using if-else statements.
def max_of_three_nums(x,y,z):
    if x >=y and x>=z :
        return x
    elif y>=x and y>=z:
        return y
    elif z>=x and z>=y:
        return z
    
print(max_of_three_nums(-2,-3,-100) )   


#Implement a function that checks if a number is prime.
def prime(n):
  if n>2:
      return False
  for i  in range(2,int(n**0.5)+1):
      if n % i == 0:
          return False
      return True

