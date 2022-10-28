n=int(input())
p=str(n)
s=0
for i in p:
    for j in p:
        if i==j:
            s+=1
if s==len(p):
    print('Unique Number')
else:
    print('Not Unique Number')