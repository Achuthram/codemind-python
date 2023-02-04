n=int(input())
l=list(map(int,input().split()))
k=[]
b=0
for i in l:
    s=0
    if i==0:
        s+=1
    i=abs(i-0)
    while i>0:
        i=i//10
        s+=1
    k.append(s)
m=min(k)
for j in l:
    t=0
    if j==0:
        t+=1
    j=abs(j-0)
    while j>0:
        j=j//10
        t+=1
    if m==t:
        b+=1
print(b)