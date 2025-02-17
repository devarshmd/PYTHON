for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    p=0
    for i in s:
        if i%2==1:
            p=1
            break
    if sum(s)%2==0 and p:
        print("YES")
    else:
        print("NO")
