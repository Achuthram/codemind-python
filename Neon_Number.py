n=int(input())
s=0
p=n*n
for i in str(p):
    i=int(i)
    s+=i
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')