n=int(input())
rev=0
p=abs(n)
while p>0:
    r=p%10
    rev=rev*10+r
    p=p//10
if n>0:
    print(rev)
else:
    print(-rev)