lst = input().split(",")
idx = input()

if "." in idx:
    raise Exception("index value is not an integer")

idx = int(idx)

for val in range(len(lst)):
    if "." in lst[val]:
        raise Exception("list value is not an integer")
    lst[val] = int(lst[val])

try:
    print(lst[idx], end="")
except:
    raise Exception("no such index")

print(" " + str(len(set(lst))))