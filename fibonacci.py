def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Enter the number of terms: "))
    print("The first {} Fibonacci numbers are:".format(n))
    for i in range(n):
        print(fibonacci(i), end=' ')

if __name__ == "__main__":
    main()