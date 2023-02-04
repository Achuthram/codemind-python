st=str(input())
a=str(input())
k=0
for i in st:
    k+=1
    s=0
    if a==i:
        s+=1
        break
if s>0:
    print('True')
    print(k-1)
else:
    print('False')