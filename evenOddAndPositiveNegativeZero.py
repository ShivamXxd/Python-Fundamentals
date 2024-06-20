n = int(input("Enter a number for even or odd: "))
n1 = int(input("Enter a number for +, - or 0: "))
if(n % 2 == 0): print("Even")
else: print("Odd")

if(n1 > 0): print("Positive.")
elif(n1 < 0): print("Negative.")
else: print("Zero")