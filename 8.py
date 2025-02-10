for i in range(int(input())):
    s=list(input().strip())
    for i in range(len(s)):
        if s[i]=='<':
            s[i]='>'
        elif s[i]=='>':
            s[i]='<'
    m=0
    for i in range(len(s)-1):
        if s[i]=='>' and s[i+1]=='<':
            m=m+1
    print(m)
