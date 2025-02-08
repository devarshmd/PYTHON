for i in range(int(input())):
    a1,b1,c1=map(int,input().split())
    a2,b2,c2=map(int,input().split())
    m1=a1+b1+c1
    m2=a2+b2+c2
    if m1==m2:
        if a1==a2:
            if b1==b2:
                if c1==c2:
                    print("Tie")
                elif c1>c2:
                    print("Dragon")
                else:
                    print("Sloth")
            elif b1>b2:
                print("Dragon")
            else:
                print("Sloth")
        elif a1>a2:
            print("Dragon")
        else:
            print("Sloth")
    elif m1>m2:
        print("Dragon")
    else:
        print("Sloth")
