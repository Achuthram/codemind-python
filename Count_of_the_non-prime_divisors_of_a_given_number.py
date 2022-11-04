n=int(input())
p=0
k=0
for i in range(1,n+1):
    if n%i==0:
        k+=1
        s=0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                s+=1
        if s==0:
            p+=1
print(k-p+1)