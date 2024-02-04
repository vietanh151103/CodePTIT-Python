for t in range(int(input())):
    s = input()
    length = len(s)
    if s[0] == s[length - 2] and s[1] == s[length - 1]:
        print("YES")
    else:
        print("NO")
