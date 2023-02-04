n,k=map(int,input().split())
l=list(map(int,input().split()))
t=0
for i in l:
    s=0
    if i==0:
        s+=1
    i=abs(i-0)
    while i>0:
        i=i//10
        s+=1
    if s==k:
        t+=1
print(t)