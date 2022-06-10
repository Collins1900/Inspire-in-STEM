#function which return reverse of a string

def isPalindrome(s):
    return s ==s[::-1]

#Drive code
s = str(input("enter number word to check if it is palindome "))
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

