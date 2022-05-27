s=0; a=int(input())
if a<7:
    print("Error")
else:
    for i in range (7, a+1):
        s=s+i
    print("7 부터 ", a ,"까지의 숫자의 합은 ", s)