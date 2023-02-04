n=int(input())
l=list(map(int,input().split()))
for i in l:
    s=0
    i=abs(i-0)
    while i>0:
        i=i//10
        s+=1
    if s!=0:
        print(s,end=' ')
    if s==0:
        print(1,end=' ')

        