n = int(input("Enter a number: "))
flag = 0
for i in range(2, n//2 + 1):
    if(n % i == 0):
        flag = 1
        break

if(flag): print("Not a prime.")
else: print("Prime number.")