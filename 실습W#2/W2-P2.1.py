m=int(input())
if m<=1200:
    k=m*6/100.0
    print("소득 %f 만원의 세금은 %f 만원, 세후소득은 %f 만원" %(m,k,m-k))
elif m<=4600:
    k=1200*6/100.0+(m-1200)*15/100.0
    print("소득 %f 만원의 세금은 %f 만원, 세후소득은 %f 만원" %(m,k,m-k))
elif m<=8800:
    k=1200*6/100.0+(4600-1200)*15/100.0+(m-4600)*24/100.0
    print("소득 %f 만원의 세금은 %f 만원, 세후소득은 %f 만원" %(m,k,m-k))
elif m<=15000:
    k=1200*6/100.0+(4600-1200)*15/100.0+(8800-4600)*24/100.0+(m-8800)*35/100.0
    print("소득 %f 만원의 세금은 %f 만원, 세후소득은 %f 만원" %(m,k,m-k))
else :
    k=1200*6/100.0+(4600-1200)*15/100.0+(8800-4600)*24/100.0+(15000-8800)*35/100.0+(15000-m)*38/100.0
    print("소득 %f 만원의 세금은 %f 만원, 세후소득은 %f 만원" %(m,k,m-k))