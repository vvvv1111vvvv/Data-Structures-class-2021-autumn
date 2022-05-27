'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.28

1. 목적:  고급정렬의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 11.3: 입력 리스트가 영어 문자열로 이루어져있다.
        이  리스트를 카운팅 정렬을 이용해 정렬하는 코드를 작성하라
3. 방법 : 12.8절의 함수와 테스트 코드를 응용한다.

카운팅 정렬: 1.  정렬을 위한 키 값들이 일정한 범위를 가진 정수일때 사용
            2.  킷값을 가진 항목의 수를 세는 방법을 사용한다, (비교연산 X)

알고리즘
#1. 문자열을 입력받는다.
#2. 정렬되지 않은 문자열을 출력
#3. 문자열 정렬을 위한 counting_sort()함수를 호출/ 매개변수 :a
    #3-1.정렬 결과를 저장 하는 배열 output fmf 선언및 초기화
    #3-2.각 문자의 빈도를 저장하는 배열 count 선언 및 초기화
    #3-3. for문 : 각 문자별 빈도 계산 , 각 데이터의 문자를 유니코드로 변환하여 해당하는 count리스트의 idx의 데이터를 +1 한다.
    #3-4. for문 : cout[i]가 출력배열에서 해당 문자의 위치가 되도록 수정
    #3-5. for문 : 정렬된 배열 만들기
    #3.6. for문 : 정렬 결과를 원래 배열에 복사, 유니코드 값을 문자로 변환하는 함수
#4. 정렬된 문자열을 출력
'''
MAX_VAL=1000
def counting_sort(A):
    output=[0]*MAX_VAL      #정렬 결과를 저장 하는 배열 output fmf 선언및 초기화
    count=[0]*MAX_VAL       #각 문자의 빈도를 저장하는 배열 count 선언 및 초기화

    for i in A:             #각 문자별 빈도 계산
        count[ord(i)]+=1    #ord() : 문자를 유니코드값으로 변환하는 함수
    for i in range(MAX_VAL):    #cout[i]가 출력배열에서
        count[i]+=count[i-1]    #해당 문자의 위치가 되도록 수정
    for i in range(len(A)):     #정렬된 배열 만들기
        output[count[ord(A[i])]-1]=ord(A[i])
        count[ord(A[i])]-=1
    for i in range(len(A)):     #정렬 결과를 원래 배열에 복사
        A[i]=chr(output[i])     #chr(): 유니코드 값을 문자로 변환하는 함수



a=list(input())     #문자열을 입력한다.
print(a)            #정렬되지 않은 문자열을 출력
counting_sort(a)    #문자열 정렬을 위한 counting_sort()함수를 호출/ 매개변수 :a
print(a)            #정렬된 문자열을 출력