numbers = [1,1,1,9,1]
is_one = False
rep_number = numbers[0]

for el in numbers:
    if rep_number == el:
        is_one = True
        rep_number = el
    else:
        is_one = False
        break

print(is_one)