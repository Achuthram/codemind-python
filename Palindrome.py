n=int(input())
k=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==k:
    print('True')
else:
    print('False')