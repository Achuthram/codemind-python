n=int(input())
p=n*n
s=0
for i in str(p):
    i=int(i)
    s+=i
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')