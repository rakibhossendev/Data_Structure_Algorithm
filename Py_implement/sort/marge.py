def merge_sort(array): # 1,3,4,5,2

    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    
    left_half = array[:mid]
    right_half = array[mid:]
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_array(left,right)
 

def merge_array(left,right):
    result = [] # 1 2
    i,j=0,0
    n,m=len(left),len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < len(right):
            result.append(left[i])
            i += 1

    if j < m:
        while j < len(right):
            result.append(right[j])
            j += 1

    return result

array = [1,3,4,5,2]
result = merge_sort(array)
print(result)


