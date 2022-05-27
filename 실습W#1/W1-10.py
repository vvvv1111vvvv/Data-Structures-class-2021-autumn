
while True:
    k=int(input("인수를 구하고 싶은 자연수를 입력하세요 "))
    if k==0:
        print("0을 입력하셨습니다. 프로그램을 종료합니다")
        break
    elif k==1:
        print(" 1대신 다른 자연수를 입력하세요\n")
        pass
    else:
        n=1
        while True:
 
            if k==n:
                print("이상 종료합니다\n")
                break
            elif k%n==0 and n!=1:
                print(n,end=" ")
                n+=1
            else:
                n+=1
        pass
