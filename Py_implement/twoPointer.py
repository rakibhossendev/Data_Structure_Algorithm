numbers = [1,2,3,4,5,6,7]
left = 0
right = len(numbers) - 1
target = 9

while left < right:
    current_sum = numbers[left] + numbers[right]

    if target == current_sum:
        print(left)
        print(right)
        break

    elif target > current_sum:
        left += 1
    else:
        right -= 1



'''numbers = list(range(1,100000))
target = 10000

i = 0
while i < len(numbers):
    j = 0
    while j < len(numbers):
        currnet_sum = numbers[i] + numbers[j]

        if target == currnet_sum:
            print(currnet_sum)

        j += 1

    i += 1'''

