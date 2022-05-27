a=0
while True:
    k=int(input("구구단을 원하는 숫자를 입력하세요"))
    if k<=0 or k>10:
        print("ERROR")
    else:
        for a in range(1,10):
            print(k, " X ",a ," = ", a*k)
        break

