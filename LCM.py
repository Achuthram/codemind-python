n1,n2=map(int,input().split())
if n1>n2:
    g=n1
else:
    g=n2
while 4:
    if g%n1==0 and g%n2==0:
        lcm=g
        break
    g+=1
print(lcm)
