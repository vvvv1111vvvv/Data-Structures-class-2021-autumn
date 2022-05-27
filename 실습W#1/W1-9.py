n=1; 
while True:
    k=int(input("인수를 구하고 싶은 자연수를 입력하세요 "))
    if k<=1:
        print("ERROR\n1 대신 다른 수를 입력해야 합니다.\n")
        pass
    else:
        break

while True:
    if k==n:
        print("이상 종료합니다")
        break
    elif k%n==0 and n!=1:
        print(n,end=" ")
        n+=1
    else:
        n+=1
