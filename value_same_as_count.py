n=int(input())
l=list(map(int,input().split()))
k=[]
v=0
b=0
for i in l:
    s=0
    for j in l:
        if i==j:
            s+=1
    if s==i:
        k.append(i)
arr=[]
for r in k:
    if r not in arr:
        arr.append(r)
print(len(arr))