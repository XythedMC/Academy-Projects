num = int(input("Enter a number: "))
nums = []
while num > 0:
    nums.append(num)
    num = int(input("Enter a number: "))

num = int(input("Enter a number: "))

res = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == num:
            res = True
            break

print(res)