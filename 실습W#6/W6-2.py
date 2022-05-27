'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.10.15

1. 목적: 연결된 구조를 활용하는 방법에 대해 실습한다.
2. 문제 : 6.3절의 연결된 리스트 클래스에 merge()연산을 구현하라
            리스트 A와 B가 있을 때, A.merge(B)는 연결리스트 A의 맨 뒤에 B를 추가하는 연산이다. 
            A의 길이는 늘어나고 B의 길이는 0이 되도록 하라

3. 방법 : 1. p6.3절의 연결된 리스트 알고리즘을 활용한다.
          2. 두 연결된 리스트 간에 노드를 이어준다;.
알고리즘:
#1. 두 개의 연결된 리스트를 임의로 만든다.
#2. 리스트 A의 노드가 리스트 B의 head를 가리키도록 한다.
#3. 리스트 B를 초기화 한다.
#4. merge()된 리스트를 출력한다.
'''

class Node():
    def __init__(self,elem,link=None):
        self.link=link
        self.data=elem


class LinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def clear(self):
        self.head=None
    def size(self):         # 1부터 시작
        n=self.head
        count=0
        while not n==None:
            n=n.link
            count+=1
        return count
    def display(self,msg="LinkedList"):
        print(msg,end=' ')
        n=self.head
        while not n==None:
            print(n.data,end=' ')
            n=n.link
        print()
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
    def insert(self,pos, elem):
        before=self.getNode(pos-1)
        if before==None:
            self.head=Node(elem,self.head)
        else: 
            n=Node(elem,before.link)
            before.link=n
    def delete(self,pos):
        before=self.getNode(pos-1)
        if before==None:
            if self.head is not None:
                self.head=self.head.link
        elif before.link !=None:
            before.link=before.link.link
    def merge(self, addingList):

        n=self.getNode(self.size()-1)
        n.link=addingList.head
        addingList.clear()



#1. 두 개의 연결된 리스트를 임의로 만든다.
A=LinkedList()
B=LinkedList()
A.insert(0,20)
A.insert(0,30)
A.insert(1,18)
B.insert(0,11)
B.insert(0,23)
B.insert(1,27)
B.insert(2,89)

A.display()
B.display()

#2. 리스트 A의 노드가 리스트 B의 head를 가리키도록 한다.  리스트 B를 초기화 한다.
A.merge(B)

#3. merge()된 리스트를 출력한다.
A.display()
B.display()