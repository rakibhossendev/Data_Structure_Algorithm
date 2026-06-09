n = int(input())
protin_value = 1

arr = list(map(int, input().split()))

for a in arr:
    protin_value *= a

root_value = int(protin_value ** 0.5)

if root_value * root_value == protin_value:
    print("Yes")
else:
    print("No")