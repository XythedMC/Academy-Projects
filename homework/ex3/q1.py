num = int(input("Enter a number: "))
nums = []

while num > 0:
    nums.append(num)
    num = int(input("Enter a number: "))

low = int(input("Enter the low:"))
high = int(input("Enter the high:"))

res = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(nums,i,j,abs(i - j))
            if abs(i - j) <= high and abs(i - j) >= low:
                res = True
                break

print(res)



