for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=0
    c=0
    d=0
    for i in range(n):
        b=b+a[i]
        if b>=k:
            b=b-k
            c=c+1
        else:
            c=c+1
            d=1
            break
    if d:
        print("NO",c)
    else:
        print("YES")
