l=list(map(str,input().split()))
k=[]
for i in l:
    s=0
    for j in i:
        s+=1
    k.append(s)
print(max(k))