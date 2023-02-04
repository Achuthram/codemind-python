l=list(map(str,input().split()))
for i in l:
    s=''
    for ch in i:
        s=ch+s
    print(s,end=' ')