n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    s+=l[i]
if s%2==0:
    print(1)
else:
    print(0)