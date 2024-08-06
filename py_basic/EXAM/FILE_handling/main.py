# f = open("example.txt", "a")
# f.write("Woops! I have deleted the content!")
# f.write("\n writing on second line")
# f.write("\n writing on third appedn line")
# f.close()

# #open and read the file after the overwriting:
# f = open("example.txt", "r")
# print(f.read())


# f=open("example.txt","w")
# f.write("w do oveidden over data ,start here,you are not able to read or print")
# f.seek(0)
#f.read() #error
# f.close()


# f=open("example.txt","w+")
# f.write("w+  oveidden over data ,write frome along here but it,but your are able to print it right ")
# f.seek(0)
#print(f.read()) #wroking
# f.close()


# f=open("example.txt","w")
# f.write("Hello")
# lst=["Boston\n","Toranto\n","sydney\n","mumbai\n","florida\n"]
# f.writelines(lst)
# f.close()


# with open("example.txt","r") as f :
#    print( f.readlines())




#write a program to read a file line by line strore into a list
def read_file_to_list(f):
    lst=[]
    with open(f , "r") as f1:
        while True :
            line=f1.readline()
            if not line:
                break
            lst.append(line.strip())  #strip() ->remove spaces
        
    return lst
        

print(read_file_to_list("example.txt"))        


# file1=open("example.txt","r")
# file_content=""
# for line in file1:
#     file_content+=line
#     file1.close()
#     print(file_content)
#     print(type(file_content))



#write a program to read entire text file 