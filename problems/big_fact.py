N = int(input())
def big_fact(N):
    i = 1
    fact = 1
     
    if N == 0:
        fact = "0000"
        return fact
    
    while i <= N:
        fact *= i

        i += 1

    result = fact % 10000
    
    return result

print(big_fact(N))