def sum(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n + sum(n - 1)

n = int(input("Hello! If you want to know the sum of some numbers, simply put it in! "))
print(sum(n))