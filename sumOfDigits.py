n = int(input("Enter a number: "))

def sumDigits(n):
    sum = 0
    str1 = str(n)
    for i in str1:
        sum += int(i)
    return sum

print(sumDigits(n))
