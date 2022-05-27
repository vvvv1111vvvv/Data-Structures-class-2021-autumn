def Comb(n,k):
    return Facto(n)/(Facto(k)*Facto(n-k))

def Facto(n):
    a=1
    for i in range(1, n+1):
        a=a*i
    return a
n, k=input().split()
n=int(n)
k=int(k)
print(Comb(n,k))