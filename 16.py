\for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=sorted(l)
    for i in range(n-1):
        if l[i]>l[i+1]:
            p=l[i]
            l[i]=l[i+1]
            l[i+1]=p
            break
    if l==l1:
        print("YES")
    else:
        print("NO")
