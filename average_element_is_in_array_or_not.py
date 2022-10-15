t=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in l:
    s+=i
p=s//t
for i in l:
    if i==p:
        k+=1
if k>0:
    print('True')
else:
    print('False')
