def Sigma2(n):
    global sum
    if n==0:
        return sum
    else:
        sum+=float(1)/float(n)
        return Sigma2(n-1)

sum=0
n=int(input())
print("%d 부터 1/%d 까지의 합: %lf"%(1,n,Sigma2(n)))