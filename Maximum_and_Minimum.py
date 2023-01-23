n=int(input())
l=list(map(int,input().split()))
k=[]
b=0
for i in l:
    s=0
    for j in l:
        if i==j:
            s+=1
    if s==i:
        k.append(i)
    else:
        b+=1
if b==len(l):
    print(-1)
else:
    print(min(k),max(k))
        
    