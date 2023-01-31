n=int(input())
l=list(map(int,input().split()))
for num in l:   
    rev=0
    while (num!=0):
        digit = num%10
        rev=rev*10+digit
        num=num//10
    print(rev,end=' ')