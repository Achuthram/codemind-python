n=int(input())
b=n
p=0
while n>0:
    r=n%10
    n=n//10
    fac=1
    for i in range(1,r+1):
        fac=fac*i
    p+=fac
if p==b:
    print("The number {} is a strong number".format(b))
else:
    print("The number {} is not a strong number".format(b))