n=int(input())
s=0
for i in range(1,n//2):
    if i*i==n:
        s+=1
if s>0:
    print('True')
else:
    print('False')
    
    