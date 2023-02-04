l=list(map(str,input().split()))
k=['a','e','i','o','u']
m=[]
for i in l:
    s=0
    for j in i:
        if j in k:
            s+=1
    print(s,end=' ')