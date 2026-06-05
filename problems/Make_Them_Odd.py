def make_odd(numbers):
    s = 0
    if len(numbers) == 1:
        s = numbers[0]
        result = s/2
        if result%2!=0 and result==int(result):
            return 1
        else:
            return -1

    i = 0
    while i < len(numbers):
        s = numbers[i]+numbers[i+1]
        res = s/2

        if res%2!=0 and res==int(res):
            return 1
        elif res%2==0 and res==int(res):
            i += 1
            continue
        else:
            return -1

        i += 1

nums = [5,10,4]
x = make_odd(nums)
print(x)
print(nums)
