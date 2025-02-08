for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    m=0
    for i in b:
        if a.count(i)>2:
            m=1
            break
    if m:
        print("No")
    else:
        print("Yes")
