n=int(input())
l=0
while n>0:
    r=n%10
    n=n//10
    if l<r:
        l=r
print(l)