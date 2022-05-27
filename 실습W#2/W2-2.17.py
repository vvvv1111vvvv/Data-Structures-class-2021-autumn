def fib(n):

    a[n]+=1
    if n==0: return 0
    elif n==1: return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
a=[0]*(n+1)
fib(n)
for i in range(0, n+1):
    print("Fibo(%d) = %d번" %(i,a[i]))
