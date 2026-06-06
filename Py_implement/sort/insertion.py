nums = [2,1,4,5,3,6]

n = len(nums)
i = 1

while i < n:
    item = nums[i]

    j = i - 1

    while j >= 0 and nums[j] > item:
        nums[j+1] = nums[j]

        j -= 1

    nums[j+1] = item

    i += 1

print(nums)

