def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Hello! If you want to know the factorial of a number, simply put it in! "))
print(factorial(n))