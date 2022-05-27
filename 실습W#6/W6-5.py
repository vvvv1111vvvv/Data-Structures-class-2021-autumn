'''
작성자 : vvvv1111vvvv
작성일 : 2021.10.15

1. 목적: 연결된 구조를 활용하는 방법에 대해 실습한다.
2. 문제 : 연결리스트를 이용해 다항식의 유의미한 계수와 지수만 을 저장한다. 두 다항식의 합을 출력한다.

3. 방법 : p6.3절의 연결된 리스트 알고리즘을 활용한다.

알고리즘:
#1. 두개의 다항식을 입력받는다.
#2. 화면에 출력한다.
#3.
#4.
#5.

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



class Term:
    def __init__(self,expo,coef):   #다항식의 항을 나타내는 클라스
        self.expo=expo                  #항의 지수
        self.coef=coef                  #항의 계수



class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__(self)
    def read(self):

    def display(self):

    def add(self, polyB):


x1=SparsePoly()
x2=SparsePoly()
    while True:
        a= input("계수의 차수 입력(종료:-1) : ")
        if a==-1 : break
        else:
            x1.coef,x1.expo=a.split()
            x1.insert(x1.size()-1.)
