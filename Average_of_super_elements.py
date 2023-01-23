n=int(input())
l=list(map(int,input().split()))
k=[]
v=0
b=0
t=0
for i in l:
    s=0
    for j in l:
        if i==j:
            s+=1
    if s==i:
        k.append(i)
    else:
        b+=1
arr=[]
for r in k:
    if r not in arr:
        arr.append(r)
for w in arr:
    t=t+w
if b==len(l):
    print(-1)
else:
    print('{:.2f}'.format(t/len(arr)))
