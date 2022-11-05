n=int(input())
a=0
b=1
c=0
while c<n:
    c=a+b
    a=b
    b=c
if abs(a-n)<abs(c-n):
    print(a)
elif abs(a-n)>abs(c-n):
    print(c)
else:
    print(a,c,end=" ")