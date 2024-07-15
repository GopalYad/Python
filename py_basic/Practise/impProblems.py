
#1) count squares
def countSquares(N):
    cnt = 0 
    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            if j * j == i:
                cnt += 1
            j += 1
    return cnt

# Example usage:
b = 4
print(countSquares(b))  # Output should be 2, as 1 and 4 are perfect squares


def searchMany(s, x, k):
    cnt = 0 
    k_found = False
    for i in s:
        if i == x:
            cnt += 1
        if i == k:
            k_found = True
    
    print(f"Count of {x}: {cnt}")
    return k_found

print(searchMany([10, 15, 20, 30, 40], 20, 1))  # Output: Count of 20: 1, True


def triangle(N):
    for i in range(1,N+1):
        for j in range(i):
         print("*",end=' ')

        print()

N = 5
triangle(N)       


#count vowels in alphabets
def vowel_count(str):
    cnt=0
    vowel =set("aeiouAEIOU")
    for alphabets in str:
        if alphabets in vowel:
            cnt+=1
            print(cnt)

str ="GoPal"
vowel_count(str)   


#print hcf on a number
def hcf(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf

print(hcf(20, 40))  # Output should be 20
      