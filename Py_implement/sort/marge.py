def merge_array(left,right):
    result = []
    i,j=0,0
    n,m=len(left),len(right)

    while i < n and i < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    return result

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]

result = merge_array(arr1,arr2)
print(result)


