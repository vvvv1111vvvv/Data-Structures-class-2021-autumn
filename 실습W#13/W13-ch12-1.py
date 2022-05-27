'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.28

1. 목적:  고급정렬의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 12.1: 어떤 배열이 오름차순으로 정렬되어 있는지 검사하여 정렬되어 있으면 True를
            False를 반환하는 함수를 구현하라

3. 방법 :   버블정렬함수의 일부를 응용한다.


알고리즘
#1. 난수 발생함수 randint 사용을 위한 random모듈 import
#2. 데이터 저장을 위한 리스트선언 및 랜덤한 정수 10개를 리스트에 츠가
#3. 정렬안된 리스트 출력
#4. 오름차순 버블정렬 함수 sort()호출
#5. j:외부루프 리스트의 크기 -1 만큼 반복,
    i:내부루프 리스트의 크기 -1 -정렬된 수의 개수 만큼 반복
    #5-1. i번째 idx의 데이터가 i+1번째 idx의 데이터 보다 크면 교환
    #5-2. 만약 1회 회전에서 교환이 존재하지 않으면 정렬이 되어있으므로 반환
#6. 오름차순 정렬된 리스트 출력
'''
def sort(data):

    for j in range(len(data)-1):
        c=False                             #교환 정지시 탈출 하도록 설계
        for i in range (len(data)-1-j):
            if data[i]>data[i+1]:           #i번째 idx의 데이터가 i+1번째 idx의 데이터 보다 크면
                a1=data[i]                  #교환
                a2=data[i+1]
                data[i],data[i+1]=a2,a1
                c=True                      #교환 존재
        if c==False:                        #만약 1회 회전에서 교환이 존재하지 않으면
            return                              #정렬이 되어있으므로 반환
import random                                #난수 발생함수 randint 사용을 위한 random모듈 import
data=[]                                         #데이터 저장을 위한 리스트
for i in range(10):                             #랜덤한 정수 10개를 데이터에 추가
    data.append(random.randint(1,9999))
print(data)         #정렬 안된 data출력
sort(data)          #오름차순 버블 정렬함수 sort()호출
print(data)         #오름차순 버블 정렬된 리스트 출력
