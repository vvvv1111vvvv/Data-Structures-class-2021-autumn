'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.04

1. 목적: 트리의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 8.3 :  임의의 노드의 레벨을 구하는 연산을 구현하라
3. 방법 : 8.3절의 함수와 테스트 코드를 사용한다..

알고리즘
#1 노드의 레벨을 구하는 메소드 levelnode()에 root노드와,
    구하고자하는 노드의 데이터를 입력한다.
#2 노드의 레벨을 연산하는 메소드 getlevelnode()에 root노드와 노드의 데이터, level=1 을 삽입한다.
#3. 순회를 이용해 노드의 레벨을 구한뒤, 반환한다.
#4. 반환된 값을 출력한다.
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


    def getlevelnode(self,node, data,level):
        if node ==None:         #만약, 입력된 노드가 None이면 0을 반환
            return 0
        if node.data==data:     #만약, 입력된 노드의 데이터가 구하고자 하는 데이터와 동일하다면
            return level        # level을 반환
        downlevel = self.getlevelnode(node.left,data,level+1)   #위의 조건문이 실행되지 않으면, 하위 노드를 순회하여 연산

        if (downlevel != 0):        #만약 하위 레벨이 0이 아니면
            return downlevel        #하위 레벨을 반환
        downlevel = self.getlevelnode(node.right,data,level+1) #right.node의 레벨을 찾는다.
        return downlevel

    def levelnode(self,node,data):

        return self.getlevelnode(node,data,1)

print("\n[실습 8.3번 문제]")
d=TNode('D',None,None)
c=TNode('C',None,None)
b=TNode('B',c,d)
f=TNode('F',None,None)
e=TNode('E',None,f)
root=TNode('A',b,e)
print(' Pre-Order : ',end='')
root.preorder(root)
print('\n In-Order : ',end='')
root.inorder(root)
print('\n Post-Order : ',end='')
root.postorder(root)
print('\n Level-Order : ',end='')
root.levelorder(root)
print('\n level of node? : ',end='')
print("\nroot = " ,root.levelnode(root,root.data))
print("f = " ,root.levelnode(root,f.data))
print("b = " ,root.levelnode(root,b.data))
print("e = " ,root.levelnode(root,e.data))
print("d = " ,root.levelnode(root,d.data))

print()
print ("노드의 개수 = %d개" %root.count_node(root))
print ("단말의 개수 = %d개" %root.count_leaf(root))
print ("트리의 높이 = %d개" %root.calc_height(root))
