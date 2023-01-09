n=int(input())
l=[]
s=0
for i in range(2,n//2+1):
    if n%i==0:
        l.append(i)
for i in l:
    for j in l:
        if abs(i-j)==1:
            s+=1
if s>0:
    print('YES')
else:
    print('NO')
        