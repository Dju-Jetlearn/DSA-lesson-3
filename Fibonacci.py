def fibonacci(n):
    if n == 0:
        return 0
    elif n ==  1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int (input("Hello! If you want to know the fibonacci sequence of a number, simply put it in! "))

for i in range(0,n+1):
    print(fibonacci(i))