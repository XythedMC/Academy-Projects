num = int(input("Enter a number: "))
nums = []

while num > 0:
    nums.append(num)
    num = int(input("Enter a number: "))

max = -1
Idx_1 = -1
Idx_2 = -1

error = False
if len(nums) == 0:
    print("There are no such indices")
    error = True
else:
    for i in range(len(nums)):
        if nums[i] < 0:
            print("There are no such indices")
            error = True
            break
        for j in range(i + 1, len(nums)):
            if nums[j] - nums[i] > max:
                max = nums[j] - nums[i]
                Idx_1 = i
                Idx_2 = j

if not error:
    if max == -1:
        print("There are no such indices")
    else:
        print(Idx_1, Idx_2)
