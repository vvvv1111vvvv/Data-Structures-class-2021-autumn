
h=int(input())
for i in range(h,0,-1):
    for j in range (1,2*h):
        if j<i:
            print(' ',end=' ')
        elif i<=j and j<=h:
            print(2*(j-i)+1,end=' ')
        else:
            m= 2*(h-i)+1-2*(j-h)
            if m<0:
                continue
            else:
                print(m,end=' ')
    print("\n")           


