t=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
print('{:.2f}'.format(s/t))