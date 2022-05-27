'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.28

1. 목적:  고급정렬의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 11.4: 10자리 이하의 정수로 이루어진 입력 리스트가 있다. 이 리스트를 다음과 같이 정렬하라
                        (1) 16개의 버켓을 사용하는 기수정렬
                        (2) 10개의 버켓을 사용하는 기수정렬
                        (3) 2개의 버켓을 사용하는 기수정렬        
3. 방법 : 12.7절의 함수와 테스트 코드를 응용한다.


알고리즘
#1. DIGITS=4, BUCKETS=16 를 상수로 선언
#2. 1부터 9999까지의 숫자 10개 생성
#3. 기수정렬 전 data를 출력
#4. radix_sort(data) 함수를 호출
#5. 기수정렬 후 data를 출력
'''

from queue import Queue     #파이썬 queue모듈의 Queue사용
def radix_sort(A):      #기수정렬을 위한 함수/ 매개변수 : A
    queues=[]           #큐의 리스트
    for i in range(BUCKETS):    #BUCKETS개의 queue 사용
        queues.append(Queue())      #구조: [큐1, 큐2, 큐3, ... , 큐BUCKETS], 큐n=[]
    n= len(A)
    factor = 1      #1의 자리부터 시작
    for d in range(DIGITS): #모든 자리에 대해서
        for i in range(n):  #자릿수에 따라 큐에 삽입
            queues[(A[i]//factor)%16].put(A[i]) #숫자를 a삽입
        i=0
        for b in range(BUCKETS):            #버킷에서 꺼내어 원래의 리스트로
            while not queues[b].empty():    #b번쨰 큐가 비어있지 않는 동안
                A[i]= queues[b].get()       #원소를 꺼내 리스트에 저장
                i+=1
        factor *=10                         #그 다음 자릿수로 간다.
        print("step",d+1,A)

import random       #random모듈을 import

DIGITS=4

BUCKETS=16
data=[]
for i in range(10):                         #1부터 9999까지의 숫자 10개 생성
    data.append(random.randint(0,9999))
print(" ")
print("기수정렬 전 : %d, " %(BUCKETS),data)
radix_sort(data)
print("radix BUCKET: %d, " %(BUCKETS),data)
print()

