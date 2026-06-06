def insert_any_index(numbers,index,item):
    numbers.append(0)
    i = len(numbers)-1

    while i > index:
        numbers[i] = numbers[i-1]
        i -= 1

    numbers[index] = item

    return numbers

# delete
def delete(numbers,index):
    i = index
    while i < len(numbers) - 1:
        numbers[i] = numbers[i+1]
        i += 1
    numbers.pop()

    return numbers


numbers = [10,20,30,40]
delete(numbers,0)
print(numbers)


