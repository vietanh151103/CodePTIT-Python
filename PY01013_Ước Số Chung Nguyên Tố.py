import math

def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    if is_Prime(sum(int(i) for i in str(math.gcd(a, b)))):
        print("YES")
    else:
        print("NO")

            