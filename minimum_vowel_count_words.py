l=list(map(str,input().split()))
k=['a','e','i','o','u']
m=[]
t=0
for i in l:
    s=0
    for j in i:
        if j in k:
            s+=1
    m.append(s)
m1=min(m)
for e in l:
    q=0
    for f in e:
        if f in k:
            q+=1
    if q==m1:
        t+=1
print(t)
