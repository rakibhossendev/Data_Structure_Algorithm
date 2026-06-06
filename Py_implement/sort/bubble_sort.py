numbers = [2,3,6,4,1,5]

n = len(numbers)
i = 0
while i < n:
    j = 0

    while j < n - i - 1:
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

        j += 1
        
    i += 1

print(numbers)