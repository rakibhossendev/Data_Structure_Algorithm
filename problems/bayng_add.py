A = 123
B = 321

is_carry = False
while A > 0 and B > 0:
    total = A%10 + B%10

    if total >= 10:
        is_carry = True
        break
    else:
        is_carry = False

    A //= 10
    B //= 10

if is_carry:
    print("YES")
else:
    print("NO")
