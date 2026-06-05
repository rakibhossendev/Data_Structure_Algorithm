N = int(input())
def big_fact(N):
    i = 1
    fact = 1

    if N == 0 or N == 1:
        fact = 1
        return fact

    while i <= N:
        fact *= i

        i += 1

    big_fact = str(fact)
    new_fact = big_fact[-4:]

    return int(new_fact)

print(big_fact(N))
