for i in range(int(input())):
    n,a=map(int,input().split())
    m=n-a
    if m>a:
        print(a)
    else:
        print(m)
