t=int(input())
l=list(map(int,input().split()))
t=0
for i in l:
    if i%2!=0:
        t=i
print(t)