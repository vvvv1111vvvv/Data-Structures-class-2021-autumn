def Sigma(n):
    global sum
    if n==0:
        return sum
    else:
        sum+=n
        return Sigma(n-1)
sum=0
n=int(input())
print("%d 부터 %d 까지의 합은 %d" %(1,n, Sigma(n)))
