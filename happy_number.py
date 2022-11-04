n=int(input())
s=0
while n>9:
    s=0
    while n>0:
        r=n%10
        n=n//10
        s+=(r*r)
    n=s
if n==1 or n==7:
    print('True')
else:
    print('False')