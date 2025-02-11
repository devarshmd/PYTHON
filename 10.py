for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]==1:
            m=i
        elif l[i]==n:
            p=i
        else:
            continue
    if m<p:
        x=m+(n-1-p)
    else:
        x=m+(n-1-p)-1
    print(x)
