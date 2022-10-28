a=int(input())
b=int(input())
s=0
p=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        p+=j
if a==p and b==s:
    print('Amicable')
else:
    print('Not Amicable')