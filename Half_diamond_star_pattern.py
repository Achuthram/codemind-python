n=int(input())
if n<=2:
    print('The pattern is not possible')
else:
    for i in range(1,n):
        print('*'*i)
    while n>0:
        print('*'*n)
        n=n-1