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
