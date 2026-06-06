def linear_search(array,x):
    i = 0

    while i < len(array):
        if array[i] == x:
            return i

        i += 1

print(linear_search([10,2,3,4,6,7],2))
