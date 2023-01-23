n=int(input())
l=list(map(int,input().split()))
s=0
arr=[]
for i in l:
    if i not in arr:
        arr.append(i)
for j in arr:
    if j%2==0:
        s+=1
print(s)