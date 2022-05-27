i=0; sum=0
while True:
    i= int(input("숫자를 입력하세요\n"))
    if i!=0:
        sum+=i
    else:
        print("입력된 정수의 합은 : "+ str(sum)+" 입니다",end="고생하셨습니다")
        break
    
