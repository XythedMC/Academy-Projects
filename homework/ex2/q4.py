ssn = input("enter the ssn: ")

nums = []
for i in range(len(ssn)):
    nums.append(int(ssn[i]))

nums_sum = []
sum = 0
for i in range(len(nums)):
    if i % 2 == 0:
        nums_sum.append(nums[i])
    else:
        temp = nums[i] * 2
        if temp > 9:
            nums_sum.append(temp // 10)
            nums_sum.append(temp % 10)
        else:
            nums_sum.append(temp)

for i in nums_sum:
    sum += i
sum -= nums[-1]

rightmost = 0
while sum % 10 != 0:
    sum += 1
    rightmost += 1

if int(ssn[-1]) == rightmost:
    print(True)
else:
    print(False)