import random
answer=random.randrange(0,99)
min=0;max=99
for i in range(0,10):
    print("숫자를 입력하세요 범위: %d~%d :" %(min,max))
    guess=int(input())
    if answer==guess:
        print("정답입니다. ", i+1 ,"번 만에 맞췄습니다.")
        break
    elif answer <= guess:
        print("더 작은 숫자입니다.")
        max=guess-1
    else:
        print("더 큰 숫자입니다.")
        min=guess+1
