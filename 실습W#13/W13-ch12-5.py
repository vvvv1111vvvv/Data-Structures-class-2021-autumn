'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.28

1. 목적:  고급정렬의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 12.5: 나만의 하이브리드 정렬 알고리즘을 구현해 보자
            입력리스트가 주어지면 이를 크기가 32인 부분리스트로 분활하고 각 부분 리스트를 선택정렬을
            이용해 정렬한한다. 각 부분리스트가 모두 정렬되면 다음으로 병합정렬의 병합과정을 이용해 부분리스트를
            병합한다. 병합이 이루어질때마낟 부분배열의 크기가 두배가된다.

3. 방법 : 12장의 함수와 테스트 코드를 응용한다.


알고리즘
#1. 난수 발생함수 randint 사용을 위한 random모듈 import
#2. 데이터 임시 저장을위한 리스트 sorted와 데이터 저장을 위한 리스트 data를 선언
#3. 랜덤한 정수 32개를 데이터에 추가
#4. 정렬되지 않은 데이터 출력
#5. 데이터 임시 저장을위한 리스트를 0으로 초기화
#6. 데이터 정렬을 위한 함수 merge_sort()를 호출
    #6-1. selection_sort()함수를 호출
        #6-1-1. 32개로 분활된 입력 배열에서 두 연속된 데이터를 비교
            연속된 두 쌍에 대하여 앞의 값이 더 크면	교환한다.
    #6-2. left와 right사이의 갭을 나타내는 변수 gap 선언및 초기화
    #6-3. gap의 제곱연산을 위한 변수  n의 선언및 초기화
    #6-4. while문 :merge연산을 종료하는 조건:전체 배열에대해 merge연산이 끝났을때
        #6-4-1. 병합연산
        #6-4-2. 분할된 데이터들의 병합이 끝났으면, gap을 증가시킨다
        #6-4-3. n을 1증가
'''

def selection_sort(A) :			#선택정렬   32개로 분활된 입력 배열에서 두 연속된 데이터를 비교
    n = len(A)
    for j in range(0,n-1,2) :   #연속된 두 쌍에 대하여
        if (A[j]>A[j+1]) :		#앞의 값이 더 크면
            A[j], A[j+1] = A[j+1], A[j]		 #교환

def merge_sort(A,left,right):
    '''
    병합정렬 알고리즘을 이용해 배열을 오름차순으로 정렬하는 함수
    입력: A:배열, left: 좌측인덳,, right: 우측 인덱스
    리턴: 없음
    '''
    selection_sort(A)       #선택정렬 함수를 호출
    gap=3                   #left와 right사이의 갭을 나타내는 변수 gap 선언및 초기화
    n=2                     #gap의 제곱연산을 위한 변수  n의 선언및 초기화
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
for i in range(32):                             #랜덤한 정수 32개를 데이터에 추가
    data.append(random.randint(1,9999))
print("정렬 전: ", data)                    #정렬되지 않은 데이터 출력
sorted=[0]*len(data)                        #데이터 임시 저장을위한 리스트를 0으로 초기화
merge_sort(data,0,len(data)-1)              #데이터 정렬을 위한 함수 merge_sort()를 호출
print("정렬 후: ", data)                     #정렬된 데이터 출력
