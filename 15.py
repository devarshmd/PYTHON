for i in range(int(input())):
    n=int(input())
    s=list(input().strip())
    if s.count('I')>0:
        print("INDIAN")
    elif s.count('Y')>0:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
