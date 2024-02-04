import math

for t in range(int(input())):
    s = input().split()
    n, x, m = [float(i) for i in s]
    # m = n * (1 + x/100) ^ res
    # log(a, N) = M <=> N = a ^ M
    res = math.log(m/n, 1 + x/100)
    print(math.ceil(res))