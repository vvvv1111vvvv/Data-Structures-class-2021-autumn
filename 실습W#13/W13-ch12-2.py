'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.28

1. 목적:  고급정렬의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 12.2: 12.4절의 병합정렬을 순환이 아니라 반복을 이용하여 다시 구현하라, 
3. 방법 : 12.4절의 함와 테스트 코드를 응용한다.

병합정렬: 하나의 리스트를 두개의 균등한 크기로 분할하고, 분할된 부분 리스트를 정렬한다음
        두 리스트를 합하여 전체가 저열된 리스트를 만드는 방법 (분할 정복)

알고리즘
#1. 난수 발생함수 randint 사용을 위한 random모듈 import
#2. 데이터 임시 저장을위한 리스트 sorted와 데이터 저장을 위한 리스트 data를 선언
#3. 랜덤한 정수 8개를 데이터에 추가
#4. 정렬되지 않은 데이터 출력
#5. 데이터 임시 저장을위한 리스트를 0으로 초기화
#6. 데이터 정렬을 위한 함수 merge_sort()를 호출
    #6-1. left와 right사이의 갭을 나타내는 변수 gap 선언및 초기화
    #6-2. gap의 제곱연산을 위한 변수  n의 선언및 초기화
    #6-3. while문 :merge연산을 종료하는 조건:전체 배열에대해 merge연산이 끝났을때 
        #6-3-1. 병합연산
        #6-3-2. 분할된 데이터들의 병합이 끝났으면, gap을 증가시킨다
        #6-3-3. n을 1증가
'''
def merge_sort(A,left,right):
    '''
    병합정렬 알고리즘을 이용해 배열을 오름차순으로 정렬하는 함수
    입력: A:배열, left: 좌측인덳,, right: 우측 인덱스
    리턴: 없음
    '''
    gap=1                   #left와 right사이의 갭을 나타내는 변수 gap 선언및 초기화
    n=1                     #gap의 제곱연산을 위한 변수  n의 선언및 초기화
    while len(A)>2**(n-1):   #merge연산을 종료하는 조건:전체 배열에대해 merge연산이 끝났을때 
        for i in range(0,len(A)-gap,gap+1):       #for문: 병합연산
            left=i
            right=left+gap
            mid=(left+right)//2
            merge(A,left,mid,right)         #merge()함수를 호출하여 분할된 데이터를 병합
        gap=2**(n+1)-1  #분할된 데이터들의 병합이 끝났으면, gap을 증가시킨다
        n+=1

def merge(A,left,mid,right):
    '''
    두 배열을 병합정렬하는 함수(배열 A에서 병합하고자 부분의 left~right를 입력한다.)
    입력: A:배열, left: 좌측인덱스, right: 우측 인덱스
    반환: 없음
    '''
    global sorted   #병합을 위한 추가적인 배열
    k=left          #배열C(정렬된 리스트)의 인덱스
    i=left          #배열A의 인덱스
    j=mid+1         #배열 B의 인덱스
    while i<=mid and j<=right:  #배열 A와 B에서 i번째 데이터와, j번째 데이터를 비교한다. 작은 데이터를 배열 C에 추가
        if A[i]<=A[j]:
            sorted[k]=A[i]  #배열 C에 더 작은 데이터를 추가
            i,k=i+1,k+1
        else:
            sorted[k]=A[j]
            j,k=j+1,k+1
    if i>mid:   #배열 A가 배열 C에 모두 삽입되고, 배열 B가 남았을때.
        sorted[k:k+right-j+1]=A[j:right+1]
    else: 
        sorted[k:k+mid-i+1]=A[i:mid+1]
    A[left:right+1]=sorted[left:right+1] 


import random                                #난수 발생함수 randint 사용을 위한 random모듈 import
sorted=[]                                       #데이터 임시 저장을위한 리스트
data=[]                                         #데이터 저장을 위한 리스트
for i in range(8):                             #랜덤한 정수 8개를 데이터에 추가     
    data.append(random.randint(1,9999))
print("정렬 전: ", data)                    #정렬되지 않은 데이터 출력
sorted=[0]*len(data)                        #데이터 임시 저장을위한 리스트를 0으로 초기화
merge_sort(data,0,len(data)-1)              #데이터 정렬을 위한 함수 merge_sort()를 호출
print("정렬 후: ", data)                     #정렬된 데이터 출력

