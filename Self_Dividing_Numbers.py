a=int(input())
b=int(input())
for n in range(a,b+1):
    l=len(str(n))
    t=n
    s=0
    while n>0:
        r=n%10
        n=n//10
        if r==0:
            continue
        if t%r==0:
            s+=1
    if s==l:
        print(t,end=' ')