n=int(input())
l=list(map(int,input().split()))
s=0
p=0
for i in range(n):
    if i<(n-1)/2:
        s=s+l[i]
    else:
        p=p+l[i]
print(s)
print(p)