numbers = [1,2,3,4,5,6]
x = 1
left = 0
right = len(numbers) - 1

while left < right:
    mid = (left+right)//2 # 2, 1 ,0

    if numbers[mid] == x: # 3 == 1, 1 == 1
        print(mid)
        break

    if numbers[mid] < x: # 3 < 1
        left = mid + 1
    else:
        right = mid - 1 # right = 1

