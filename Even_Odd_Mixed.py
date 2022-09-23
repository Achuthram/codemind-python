n=int(input())
p=len(str(n))
e=0
o=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        e+=1
    else:
        o+=1
if e==p:
    print('Even')
elif o==p:
    print('Odd')
else:
    print('Mixed')