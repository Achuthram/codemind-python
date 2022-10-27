n=int(input())
a=0
b=1
s=0
for i in range(n):
    c=a+b
    a=b
    b=c
    if c==n:
        s+=1
if s>0:
    print('True')
else:
    print('False')