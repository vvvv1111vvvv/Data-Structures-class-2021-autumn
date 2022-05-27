while True:
    k=int(input("양의 정수를 입력하세요\n"))
    if k<=0:
        print("ERROR")
    else:
        print("결과값의 2배는 "+ str(2*k)+ " 입니다")
        break