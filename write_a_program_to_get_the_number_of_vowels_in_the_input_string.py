st=str(input())
l=['a','e','i','o','u','A','E','I','O','U']
s=0
for i in st:
    if i not in l:
        s+=1
l=len(st)
print(l-s)