
a, k, n = [int(i) for i in input().split()]
check = []
print(a, k ,n)
for b in range(1, n + 1, 1):
    if a + b % k == 0:
        check.append(b)
if len(check) > 0:
    print(check)
else:
    print(-1)