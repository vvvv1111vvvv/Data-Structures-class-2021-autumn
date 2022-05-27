'''
작성자: vvvv1111vvvv
작성일 2021.09.30

1. 목적: 스택을 활용하는 방법에 대해 실습한다.
2. 문제: 4.3-2절 스택의 구현
3. 방법: 4.2절에서 설명된 스택의 함수와 추상자료형의 활용

알고리즘:
1. 문자를 키보드로부터 입력받는다.
2. 입력받은 문자열의 각 숫자를 스택에  push()한다.
3. 스택으로부터 문자를 pop()하여 화면에 출력한다,
4. 스택의 내용을 출력한다.
'''


top=[] #스택의 데이터: 항목을 위한 공백 리스트

def isEmpty():
    '''
    함수명 : isEmpty()
    목적 : 함수의 길이 구하기
    입력 : 없음
    returns : 스택 top의 길이 : len(top)
    '''
    return len(top)==0
def push(item):
    top.append(item)
    '''
    함수명 : push(item)
    목적 : 스택 top 의 맨 위에 item 추가하기
    입력 : item
    returns : 없음
    부수효과 : 스택 top 의 맨 위에 item 추가
    '''
def pop():
    if not isEmpty():
        return top.pop(-1)
def peek():
    if not isEmpty():
        return top[-1]
def size():
    return len(top)
def clear():
    global top
    top=[]

for i in ['철수', '영희', '사과', '배', '곰']:
    push(i)
print("push 5회 :", top)
print("pop()==> ",pop())
print("pop()==> ",pop())
print("pop 2회 ==> ",top)
