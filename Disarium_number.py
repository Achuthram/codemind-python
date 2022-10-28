n=int(input())
p=n
s=0
l=len(str(n))
while n>0:
    r=n%10
    n=n//10
    s=s+(r**l)
    l-=1
if s==p:
    print('True')
else:
    print('False')