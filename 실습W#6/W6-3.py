'''
작성자 : vvvv1111vvvv
작성일 : 2021.10.15

1. 목적: 연결된 구조를 활용하는 방법에 대해 실습한다.
2. 문제 : 연결리스트를 이용한 연결된 큐 클래스를 구현하라, 데이터 맴버로
        전단을 가리키는 front와 후단을 가리키는 rear를 사용한다.삽입은 후단을 통해
        삭제는 전단을 통해 이루어 지도록 하라

3. 방법 : 1. p6.3절의 연결된 리스트 알고리즘을 활용한다.
          2. p6.4절의 연결된 큐의 구조도를 활용한다.
알고리즘:
#1. enqueue() : elememt를 후단에 삽입한다.
#2. dequeue() : front에서 데이터 1개를 꺼내 반환한다.
#3. enqueue()연산을 한뒤 dequeue()연산을 한다.
#4 결과를 display()로 출력한다
'''

class Node():
    def __init__(self,elem,link=None):
        self.link=link
        self.data=elem


class LinkedQueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        return None==self.front #front가 None 일때 Empty로 한다.
    def clear(self):
        self.front=None
    def size(self):         # 1부터 시작
        n=self.front
        count=0
        while not n==None:
            n=n.link
            count+=1
        return count
    def display(self,msg="Linkedqueue"):
        print(msg,end=' ')
        n=self.front
        while not n==None:
            print(n.data,end=' ')
            n=n.link
        print()
        '''
    def getNode(self,pos):          #pos번째 노드의 노드 반환
        if pos<0:
            return None
        n=self.front
        while pos>0 and n!=None:
            n=n.link
            pos-=1
        return n
    def getEntry(self,pos):     #pos번째 노드의 데이터 반환
        n=self.getNode(pos)
        if n==None:
            return None
        else:
            return n.data
    def replace(self,pos,elem):
        n=self.getNode(pos)
        if n==None:
            return None
        else: n.data=elem

    def find(self,elem):
        n = self.head
        while n is not None:
            if n.data==elem:
                return n
            n=n.link
        return None
        '''
#1. enqueue() : elememt를 후단에 삽입한다.
    def enqueue(self, elem):
        if self.isEmpty():
            self.front=self.rear=Node(elem,None)
        else:
            n=Node(elem,None)
            self.rear.link=n
            self.rear=n
#2. dequeue() : front에서 데이터 1개를 꺼내 반환한다.
    def dequeue(self):
        if not self.isEmpty():
            da = self.front.data
            self.front=self.front.link
            if self.front== None:
                self.rear=None
            return da


#3. enqueue()연산을 한뒤 dequeue()연산을 한다.
A=LinkedQueue()
for i in range(6):
    A.enqueue(i)
    A.display()
for i in range(2):
    A.dequeue()

#4 결과를 display()로 출력한다
A.display()
