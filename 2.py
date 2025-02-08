for i in range (int(input())):
    n=int(input())
    s=list(input().strip())
    l=['a','e','i','o','u']
    m=0
    for i in s:
        if i not in l:
            m=m+1
        else:
            m=0
        if m==4:
            break
    if m==4:
        print('NO')
    else:
        print('YES')
