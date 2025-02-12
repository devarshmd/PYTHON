for i in range(int(input())):
    n=int(input())
    a=list(input().strip())
    b=list(input().strip())
    a1=a.count('1')
    a2=a.count('0')
    b1=b.count('1')
    b2=b.count('0')
    if a1==b1 and a2==b2:
        print('YES')
    else:
        print('NO')
