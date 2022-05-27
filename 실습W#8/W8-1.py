'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.04

1. 목적: 트리의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 8.1 :    1. 트리를 연결된 구조로 표현하고
                       2. 네가지 순회방법으로 노드를 방문한 결과를 출력
                        3. 각 트리의 노드 개수와 단말노드의 개수및 트리의 높이 출력

3. 방법 : 8.3절의 함수와 테스트 코드를 사용한다..


'''
max_size=30
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

class TNode:
    '''
    목적: 이진트리를 위한 노드 클래스
    '''
    def __init__(self,data,left,right):
        self.data=data      #노드의 데이터
        self.left=left      #왼족 자식을 위한 링크
        self.right=right    #오른쪽 자식을 위한 링크
    def preorder(self,n):    #VLR 전위 순회
        if n is not None:
            print(n.data,end='')
            self.preorder(n.left)
            self.preorder(n.right)
    def inorder(self,n):    #LVR 중위 순회
        if n is not None:
            self.inorder(n.left)
            print(n.data,end='')
            self.inorder(n.right)
    def postorder(self,n):    #LRV 후위 순회
        if n is not None:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.data,end='')
    def levelorder(self,root):        #레벨 순회
        self.queue=CircularQueue()    #원형 큐 객체 초기화
        self.queue.enqueue(root)     #초기에는 루트 노드만 들어 있음
        while not self.queue.isEmpty():  #큐가 공백이 아닌동안
            n=self.queue.dequeue()       #큐에서 맨 앞의 노드n을 꺼낸다.
            if n is not None:
                print(n.data,end='')        #먼저 노드의 정보를 출력
                self.queue.enqueue(n.left)       #n의 왼쪽 자식노드를 큐에 삽입
                self.queue.enqueue(n.right)      #n의 오른쪽 자식노드를 큐에 삽입
    def count_node(self,n):             #노드 개수
        if n is None:
            return 0
        else:
            return 1+self.count_node(n.left)+self.count_node(n.right)
    def count_leaf(self,n):             #단말 노드 개수
        if n is None:
            return 0
        elif  n.left is None and n.right is None:
            return 1
        else: return self.count_leaf(n.left)+self.count_leaf(n.right)
    def calc_height(self,n):        #트리 높이 개수
        if n is None:
            return 0
        hLeft=self.calc_height(n.left)
        hRight=self.calc_height(n.right)
        if (hLeft>hRight):
            return hLeft+1
        else:
            return hRight+1
print("\n[실습 8.1 - 1 번 문제]")
d=TNode('D',None,None)
b=TNode('B',d,None)
g=TNode('G',None,None)
h=TNode('H',None,None)
e=TNode('E',g,h)
f=TNode('F',None,None)
c=TNode('C',e,f)
root=TNode('A',b,c)
print(' Pre-Order : ',end='')
root.preorder(root)
print('\n In-Order : ',end='')
root.inorder(root)
print('\n Post-Order : ',end='')
root.postorder(root)
print('\n Level-Order : ',end='')
root.levelorder(root)
print()
print ("노드의 개수 = %d개" %root.count_node(root))
print ("단말의 개수 = %d개" %root.count_leaf(root))
print ("트리의 높이 = %d개" %root.calc_height(root))

print("\n[실습 8.1 - 2 번 문제]")
a1=TNode('A',None,None)
b1=TNode('B',None,None)
div=TNode('/',a1,b1)
c1=TNode('C',None,None)
prdt1=TNode('*',div,c1)
d1=TNode('D',None,None)
prdt2=TNode('*',prdt1, d1)

e1=TNode('E',None,None)
root2=TNode('+',prdt2,e1)

print(' Pre-Order : ',end='')
root2.preorder(root2)
print('\n In-Order : ',end='')
root2.inorder(root2)
print('\n Post-Order : ',end='')
root2.postorder(root2)
print('\n Level-Order : ',end='')
root2.levelorder(root2)
print()
print ("노드의 개수 = %d개" %root.count_node(root2))
print ("단말의 개수 = %d개" %root.count_leaf(root2))
print ("트리의 높이 = %d개" %root.calc_height(root2))
