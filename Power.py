def power(n,p):
    if p == 0 or n == 1:
        return 1
    else:
        return n*(power(n,p-1))

n = int(input("Hello! If you would like to know what something to the power of something else is, please enter the number! "))
p = int(input("Now, please input the power! "))

print(power(n,p))