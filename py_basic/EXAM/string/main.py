#String are immutable in nature

# str="racecar"
# not possibble
# str[0]='a'
# print(str)


s1="slicing"
print(s1[:])  #output : slicing
print(s1[::-1])  #output : reverse
print(s1[0:6])  #output:slicin
print(s1[-1:-5:-1])



#Filter all the numnbers in list
def filter_number(lst):
    return [word for word in lst if word.isdigit()]

print(filter_number(['123',"banana"]))


#filter all string starting with vowels
def filter_strings(lst):
    str1="aeiouAEIOU"
    return[str for str in lst if str[0] in str1 ]

print(filter_strings(["apple","bananna","aeroplane"]))    


#filter all the string that contain : agra, Rakesh, tomata, Patna
def filter_lst(text):
    noun=["agra", "Rakesh", "tomato"," Patna"]
    return[word for word in text if any(noun in word for noun in noun)]

print(filter_lst(["134","tomato"]))


#string  manipulation methods / function
s2="LiOOn123"
print(s2.capitalize())  #give a copy
print(s2.lower())        #lowercase
print(s2.upper())        #uppercase
print(s2.isnumeric())    #only check number if only present numbers  and return false if any string present
print(s2.center(12,"#"))  #add left and right base of length of string
print(s2.count('O'))      #counting the occurance of characters.
print(s2.endswith("23"))  #return true if ends with
print(s2.find('O'))   #return a first occurance index





#write a program that accepts   a sentence and  calculate the number of digits , uppercase and lowercase
def string_text(s):
    d = {"upper case": 0, "lower case": 0, "digit": 0}
    for c in s:
        if c.isupper():
            d["upper case"] += 1
        elif c.islower():
            d["lower case"] += 1
        elif c.isdigit():
            d["digit"] += 1
    return d  # This should be outside the loop

# Example usage:
sentence = "Hello World! 123"
result = string_text(sentence)
print(f"Upper case letters: {result['upper case']}")
print(f"Lower case letters: {result['lower case']}")
print(f"Digits: {result['digit']}")



 #write a program to change a  given string to  a new  string where first  and last chars have be changed
 #abcd -> dbca
def change_str(str):
   return str[-1]+str[1:-1]+str[0]

print(change_str("abcdef"))


#write a progrma to check if string is palindrome or not
def check_plaindome(str):
    rev_str=str[::-1]
    if str == rev_str:
        return True
    return False

print(check_plaindome("MOM0"))


