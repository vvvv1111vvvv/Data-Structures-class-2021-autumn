def reverse(a):

    global l
    global k

    m=a[l-1]
    a[l-1]=a[k-l]
    a[k-l]=m
    if l==k//2:
        return a
    else: 
        l+=1
        reverse(a)
        if l==k//2:
            return a
string=input()
k=len(string)
l=1
nstring=reverse(list(string))
for i in range(0,k):
    print(nstring[i],end='')