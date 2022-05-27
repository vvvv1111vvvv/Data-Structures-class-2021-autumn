'''
작성자 : vvvv1111vvvv
작성일 : 2021.10.15

1. 목적: 연결된 구조를 활용하는 방법에 대해 실습한다.
2. 문제 : 6.3절의 연결된 리스트를 이중연결리스트로 다시 구현하라
            노드는 6.5절의 DNode 클래스를 사용하면 된다.


3. 방법 : p6.3절의 연결된 리스트 알고리즘을 활용한다.

알고리즘:
#1. addrear() : elememt를 rear에 삽입한다.
#2. addfront() : elememt를 front에 삽입한다.
#3. deleterear() : rear에서 데이터 1개를 꺼내 반환한다.
#4. deletefront() :front에서 데이터 1개를 꺼내 반환한다.
#5. 각각의 동작을 실행한다.
#4 결과를 display()로 출력한다
'''

class DNode():
    def __init__(self,elem, prev=None ,next=None):
        self.prev=prev
        self.next=next
        self.data=elem


class DoubleLinkedDeque():
    def __init__(self):
        self.front=None
        self.rear=None

    def isEmpty(self):
        return self.front==None     #공백상태 front 기준
    def clear(self):
        self.front=self.rear=None
    def size(self):
        n=self.front
        count=0
        while not n==None:
            n=n.next
            count+=1
        return count
    def display(self,msg="LinkedList"):
        print(msg,end=' ')
        n=self.front
        while not n==None:
            print(n.data,end=' ')
            n=n.next
        print()
        '''
    def getNode(self,pos):          #pos번째 노드의 노드 반환
        if pos<0:
            return None
        n=self.head
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
#1. addrear() : elememt를 후단에 삽입한다.
    def addrear(self, elem):
        if self.isEmpty():
            self.front=self.rear=DNode(elem,self.rear,None)
        else:
            n=DNode(elem,self.rear,None)
            self.rear.next=n
            self.rear=n
#2. addfront() : elememt를 front에 삽입한다.
    def addfront(self, elem):
        if self.isEmpty():
            self.front=self.rear=DNode(elem,None,self.front)
        else:
            n=DNode(elem,None,self.front)
            self.front.prev=n
            self.front=n

#3. deleterear() :rear에서 데이터 1개를 꺼내 반환한다.
    def deleterear(self):
        if not self.isEmpty():
            da= self.rear.data
            self.rear=self.rear.prev
            if self.rear==None:
                self.front=None
            else:
                self.rear.next=None
            return da


#4. deletefront() : front에서 데이터 1개를 꺼내 반환한다.
    def deletefront(self):
        if not self.isEmpty():
            da = self.front.data
            self.front=self.front.next
            if self.front== None:
                self.rear=None
            else:
                self.front.prev=None
            return da
A=DoubleLinkedDeque()
A.addrear(1)
A.addfront(2)
A.addfront(34)
A.deleterear()
A.addrear(32)
A.deletefront()
A.deletefront()
A.addfront(100)
A.display()
