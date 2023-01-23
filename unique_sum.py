n=int(input())
l=list(map(int,input().split()))
arr=[]
s=0
for i in l:
    if i not in arr:
        arr.append(i)
for j in arr:
    s+=j
print(s)