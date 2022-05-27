def printNum(n,k):
    a[k]=k+1
    if n==k+1:
        return a
    printNum(n,k+1)
    return a
def printRevNum(n,k):
    b[k]=n
    if 1==n:
        return b
    printRevNum(n-1,k+1)
    return b

n=int(input())
a=list(range(n))
b=list(range(n))
#,"/n", printRevNum(n))
for i in printNum(n,0):
    print(i,end=' ')
print("\n")
for i in printRevNum(n,0):
    print(i,end=' ')