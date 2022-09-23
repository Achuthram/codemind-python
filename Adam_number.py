n=int(input())
p=n*n
rev=0
ser=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
d=rev*rev
while d>0:
    x=d%10
    ser=ser*10+x
    d=d//10
if ser==p:
    print('True')
else:
    print('False')