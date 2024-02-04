for t in range(int(input())):
    s = input()
    check = 0
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            check = -1
            break
        else:
            check = 1
    if check > 0:
        print("YES")
    else:
        print("NO")