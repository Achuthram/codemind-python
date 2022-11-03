n=int(input())
p=n*n
s=0
while n>0:
    if n%10!=p%10:
        print('Not an Automorphic Number')
        s=1
        break
    n=n//10
    p=p//10
if s==0:
    print('Automorphic Number')