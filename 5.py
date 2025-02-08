for z in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    a=1
    b=1
    for i in range(n):
        if c[i]==1:
            b= not b
    if a==b:
        print("YES")
    else:
        print("NO")
