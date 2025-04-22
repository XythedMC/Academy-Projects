num = int(input("Enter a number: "))
nums = []
while num > 0:
    nums.append(num)
    num = int(input("Enter a number: "))

max_len = -1
idx = -1
for i in range(len(nums)):
    length = 1
    previous = nums[i]
    for j in range(i + 1, len(nums)):
        if nums[j] <= previous:
            length += 1
            previous = nums[j]
        else:
            break
    if length > max_len:
        max_len = length
        idx = i

print(idx)

