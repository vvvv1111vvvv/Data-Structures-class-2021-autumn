'''
작성자: vvvv1111vvvv
작성일: 2021.10.07

1. 목적: 큐와 덱을 활용하는 방법을 실습한다.
2. 문제: 덱을 활용하여 주어진 문자열이 회문인지 여부를 판단하는 프로그램을 작성하라
3. 방법: 원형덱을 활용해 양 끝단부터 서로 비교한다.

알고리즘:
1. 문자열을 키보드로부터 입력받는다.
2. 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다.
3. 소소문자를 대문자로 처리한다.
4. 덱에 변환된 문자열을 삽입한다.
5. 덱의 front와 rear의 문자열을 하나씩 꺼내며 비교한다.
'''
max_size=20
class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[0]*max_size
    def isEmpty(self):
        return self.front==self.rear
    def clear(self):
        self.items=[]
    def isFull(self):
        return self.front==(self.rear+1)%max_size
    def enqueue(self,item):
        if not self.isFull():
            self.rear=(self.rear+1)%max_size
            self.items[self.rear]=item
    def dequeue(self):
        if not self.isEmpty():
            self.front= (self.front+1)%max_size
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.item[(self.front+1)%max_size]

class Circulardeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self,item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self):return self.peek()

    def addFront(self,item):
        if not self.isFull():
            self.items[self.front]=item
            self.front= (self.front-1)%max_size
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear=(self.rear-1)%max_size
        return item
    def getRear(self):
        return(self.items[self.rear])
def find(a):
    '''
    함수명 : find()
    목적 : 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다,
    입력 : 문자열 a
    returns : 문자열 a의 대소문자 만을 데이터로 갖는 리스트
    '''
    p=re.compile('[a-zA-Z0-9]')      # 정규표현식 [a-zA-Z0-9] 을 컴파일해 결과를 객체 p에 돌려준다.
    result = p.findall(a)            # 메소드 findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
    return result

a=Circulardeque()
import re #re모듈을 사용
#1. 문자열을 키보드로부터 입력받는다.
n=input()

#2. 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다.
n=find(n)

#3. 소소문자를 대문자로 처리한다.
for i in range (len(n)):
    n[i]=n[i].upper()

#4. 덱에 변환된 문자열을 삽입한다.
for i in n:
    a.addRear(i)

#5. 덱의 front와 rear의 문자열을 하나씩 꺼내며 비교한다.
l=(a.rear-a.front)%max_size
for i in range(0,int(l/2)):
    if a.deleteRear()!=a.deleteFront():
        print("회문이 아닙니다.")
        quit()
print("회문입니다.")
