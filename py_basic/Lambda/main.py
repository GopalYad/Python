

# A lambda function  is a small anonymous function .
# A lambda function  can take any number of arguments , but can only have one expression .


 ## syntax ::   lambda  arguments(more than once ) : expression (onely must be one)

x = lambda a : a+10
print(x(5)) 

y = lambda a , b, c ,d ,e : a+b+c+d+e
print(y(2,3,4,5,6))


## it is better to use as anymonymous function that means you can use inside another function as argument
### anymonoymous function means a function without a name.
def func(n):
    return lambda a, b ,c,d,e : (a+b+c+d+e)/n

average_of_5_values=func(5)
print(average_of_5_values(2,4,5,7,9))



str = 'gopal yadav'
upper = lambda string :string.upper()
print(upper(str))