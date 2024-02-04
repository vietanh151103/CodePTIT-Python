s = input()
Upper = 0
for i in s:
    if i.isupper():
        Upper += 1

if Upper > len(s) - Upper:
    print(s.upper())
else:
    print(s.lower())