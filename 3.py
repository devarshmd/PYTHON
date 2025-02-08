for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=[]
    for i in range(0,n):
        if l[i]<=k:
            s.append(1)
            k=k-l[i]
        else:
            s.append(0)
    for i in s:
        print(i,end='')
    print()
