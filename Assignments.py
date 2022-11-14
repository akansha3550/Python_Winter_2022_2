#Please write a program that print the first N prime numbers.
#N should be declared as a variable at the beginning of your code.

n = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, n+1):
        a = n % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(n)
    else:
        k = k - 1

    n = n + 1