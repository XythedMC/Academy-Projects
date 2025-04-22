num = int(input("enter the number: "))
finish = False

prime = True

for i in range(2, num - 1):
    if num / i == int(num / i):
        prime = False
        break

print(prime and num != 1)