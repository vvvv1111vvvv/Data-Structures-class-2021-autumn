m=0;d=0
m,d= input("m,d 형식으로 날짜를 입력하세요").split()
m=int(m); d=int(d)
if m==1:
    print(d)
elif m==2:
    print(31+d)
elif m%2==0 and m<=7:
    print((m-1)//2*30+28-30+d+m//2*31)
elif m%2==1 and m<=7:
    print(m//2*31+d+((m-1)//2-1)*30+28)
elif m%2==0:
    print(365-((12-m)//2*31+31-d+(12-m)//2*30))
else:
    print(365-((12-m)//2*30+30-d+(12-m+1)//2*31))