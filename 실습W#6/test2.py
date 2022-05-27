#연결 리스트로 리스트 구현


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
    def size(self):
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
            print(n.data,end='')
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

s=LinkedList()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)

s.display()

s.replace(2,90)

s.display()
s.delete(2)

s.delete(s.size()-1)
s.display()
s.delete(0)
s.clear()
s.display()
