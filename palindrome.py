str1 = input("Enter a string: ")
n = len(str1)
flag = 0
for i in range(n // 2):
    if(str1[i] != str1[n - i - 1]): 
        flag = 1

if(flag): print("Not a palindrome.")
else: print("Palindrome.")