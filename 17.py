for i in range(int(input())):
    a,b,x=map(int,input().split())
    if a==b:
        print("YES")
    elif (a-b)%(2*x)==0:
        print("YES")
    else:
        print("NO")
