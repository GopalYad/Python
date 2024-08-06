#write a python program to count the number of vowels in a string
def vowel_count(str):
    vowels = 'aeiouAEIOU'
    cnt = 0
    for char in str:
        if char in vowels:
            cnt += 1
    return cnt

str = input("Enter a string: ")
print("Number of vowels:", vowel_count(str))



#write a python program to remove duplicate from a list of integers
def remove_dupliacte(lst):
    return list(set(lst))

lst=[1,1,2,2,3,4,5,6,6,6]
print(remove_dupliacte(lst))   



#write a python program to find the maximum and minimum values in a tuple of integers
def max_min_tuple(tpl):
    return max(tpl),min(tpl)

tpl=(15,23,0,-100,300,1000)

print(max_min_tuple(tpl))



#write a python program to merage two dicitionaries
def merge_dicts(dict1 , dict2):
    merged_dict=dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 ={'a':1 , 'b':2}
dict2={'b':3 ,'c':4}
print(merge_dicts(dict1,dict2))


#write a python program to reverse each word in a given sentence.
def rev_sentence(sentence):
    words=sentence.split()
    rev_word=[word[::-1] for word in words]
    return " ".join(rev_word)

sentence="coding is love"
print(rev_sentence(sentence))

#write a python progam to rotate a list to the right by a given number of steps.
def rotate_list(lst,steps):
    steps=steps%len(lst)
    return lst[-steps:]+lst[:-steps]

    input_lst =[int(x) for x in input("ENTER NUMBER SEPERATED BY SPACES : ").split()]
    steps=int(input("ENter number of steps to rotate:"))
    print(rotate_list(input_lst,steps))

#write a python program that take a list of integers and returns a new list containing only the prime numbers
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True

def prime_number(lst):
    return[int(x)for x in lst if isprime(x)]

list =[1,2,3,4,5,6,7,8,9]
print(prime_number(list))


def count_frequency(str):
    cnt=0
    for  i in range(97,123):
        j=chr(i)
        for l in str:
            if j==l:
                cnt+=1
    
        print(j,":",cnt)

    

str="aabba"
print(count_frequency(str))


#write a python program factor(n) that  return a list of  all positive divisors  of N (N>=1) 
#For example  factor(6) [1,2,3,6]
              # factor(1) [1]
              # facator(13) 
              # 
def factor(n):
    list=[]
    if n>=1 :
        for i in range(1, n +1):
            if n %i==0:
                list.append(i)

    return list   

print(factor(23))    


#write a python programs, countsquares(N)
