a,b=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in l:
    if i%b!=0:
        s+=1
print(s)