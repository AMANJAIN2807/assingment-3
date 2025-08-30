def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


a = int(input("enter a number: "))
b = factorial(a)
print(f"Factorial of {a} is :{b}")

