'''N = int(input())
A = map(int, input().split())

i = 0
assending = True

while i < N:
    if A[i] > A[i + 1]:
        assending = False
        break


        
if assending:
    print("YES")
else:
    print("NO")'''

n = int(input())
a = list(map(int, input().split()))

ascending = True

for i in range(1, n):
    if a[i] < a[i - 1]:
        ascending = False
        break

if ascending:
    print("Yes")
else:
    print("No")