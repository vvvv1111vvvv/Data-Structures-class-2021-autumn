def Bio(n,k):
    if k==0 or k==n:
        return 1
    else: 
        return Bio(n-1,k-1)+Bio(n-1,k)
#def Comb(n,k):
    return Facto(n)/(Facto(k)*Facto(n-k))
#def Facto(n):
    a=1
    if n==0: return a
    else: 
        a=n*Facto(n-1)
        return a

a,b= input().split()
a=int(a)
b=int(b)
print(Bio(a,b))