n = int(input("enter the n: "))

e = 0
for i in range(n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    e += 1 / factorial

print(e)