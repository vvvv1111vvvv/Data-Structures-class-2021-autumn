'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.10.21

1. 목적: 정렬을 활용하는 방법에 대해 실습한다.
2. 문제 : 6.3절의 연결된 리스트로 구현한 리스트 클래스 LinkedList에서 리스트 항목의 정렬을 위해 sort()를 구현하라, 정렬 알고리즘으로는 버블정렬을 사용

3. 방법 : 버블정렬 알고리즘을 사용하여 주어진 리스트를 정렬한다.
          
알고리즘:
#1. LinkedList의 객체 a를 선언한뒤 수를 입력한다.
#2. LinkedList클래스의 sort() 함수를 호출한다.
#3. 입력된 리스트를 버블정렬 알고리즘을 이용해 정렬한다.
#4. 반환된 결과를 출력한다.
'''
class Node():
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class LinkedList():
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def clear(self):
        self.head=None
    def size(self):
        node=self.head
        count = 0
        while not node==None:
            node=node.link
            count+=1
        return count
    def display(self):
        node=self.head
        while not node == None:
            print(node.data,end=' ')
            node=node.link
  
        print()
    def getNode(self,pos):
        if pos<0: return None
        node= self.head
        while pos>0 and node!=None:
            node = node.link
            pos-=1
        return node
    def getEntry(self,pos):
        node=self.getNode(pos)
        if node ==None: return None
        else : return node.data
    def replace(self,pos,elem):
        node = self.getNode(pos)
        if node != None:
            node.data=elem
    def find(self, data):
        node=self.head
        while node is not None:
            if node.data==data: return node
            node=node.link
        return None
    def insert(self,pos, data):
        before=self.getNode(pos-1)
        if before==None:
            n=Node(data,self.head)
            self.head=n
        else: 
            n=Node(data,before.link)
            before.link=n
    def delete(self, pos):
        before=self.getNode(pos-1)
        if before==None:
            if self.head is not None:
                self.head=self.head.link
        elif before.link is not None: before.link=before.link.link
    def sort(self):
    #3. 입력된 리스트를 버블정렬 알고리즘을 이용해 정렬한다.
        for j in range(self.size()-1):                  #교환 정지시 탈출 하도록 설계하자
            c=False
            for i in range (self.size()-1-j):
                if self.getEntry(i)>self.getEntry(i+1):
                    a1=self.getEntry(i)
                    a2=self.getEntry(i+1)
                    self.replace(i,a2)
                    self.replace(i+1,a1)
                    c=True
                    s.display()
            if c==False:                
                return
            
            



#1. LinkedList의 객체 a를 선언한뒤 수를 입력한다.
s= LinkedList()
s.insert(0,3)
s.insert(1,11)
s.insert(0,26)
s.insert(1.,4)
s.insert(3,12)
s.insert(2,74)

s.display()
#2. LinkedList클래스의 sort() 함수를 호출한다.
s.sort()
#4. 반환된 결과를 출력한다.
print()
s.display()