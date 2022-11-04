n=int(input())
s=0
k=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        s+=1
l=len(str(n))
if s==0:
    while n>0:
        r=n%10
        n=n//10
        if r==2 or r==3 or r==5 or r==7:
            k+=1
if k==l:
    print('Mega Prime')
else:
    print('Not Mega Prime')