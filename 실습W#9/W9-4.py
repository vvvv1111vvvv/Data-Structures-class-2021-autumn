'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.11

1. 목적: 이진탐색트리의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 9.4: 9.3절의 이진탐색트리를 이용하여 우선순위 큐를 구현하고 동작을 테스트하라  
3. 방법 : 9.3 절의 함수와 테스트 코드를 응용한다.

알고리즘
#1. 실습 9-3에서 정의 했던 이진탐색트리 클래스BinarySearchTree()를 이진탐색트리를 이용한 맵 클래스 BSTMap()으로 변경한다.
#2. enqueue() : 무작위로 정렬된 배열의 element를 맵에 삽입한다.
#3. dequeue() : 삽입된 element는 이진탐색트리의 구조를 가진다.
                -1-. 우선순위가 가장 높은 key는 최대키를 탐색하는 메소드를 활용해 구한다.
                -2-. 우선순위가 가장 높은 key를 delete()한다.
                -3-. value값을 반환한다.
#4. peek() : 최대키를 탐색한 뒤 key값을 반환한다.
'''

class BSTNode():                #이진탐색트리를 위한 노드클래스
    def __init__(self,key, value):
        self.key=key        #key값
        self.value=value    #value값
        self.left=None      #왼쪽자식에 대한 링크
        self.right=None     #우측자식에 대한 링크

#1. 실습 9-3에서 정의 했던 이진탐색트리 클래스BinarySearchTree()를 이진탐색트리를 이용한 맵 클래스 BSTMap()으로 변경한다.
#이진탐색트리를 이용한 맵
class BSTMap():
    def __init__(self):
        self.root=None
    def isEmpty(self):
        return self.root==None
    def clear(self):
        self.root=None
    def size(self):
        return self.count_node(self.root)
    def search(self,key):
        return self.search_bst(self.root,key)
    def searchValue(self,key):
        return self.search_Value_bst(self.root,key)
    def findMax(self): 
        return self.search_max_bst(self.root)
    def findMin(self): 
        return self.search_min_bst(self.root)
#2. enqueue() : 무작위로 정렬된 배열의 element를 맵에 삽입한다.        
    def enqueue(self,key,value=None):          
        n=BSTNode(key,value)
        if self.isEmpty():
            self.root=n
        else:
            self.insert_bst(self.root,n)
#3. dequeue() : 삽입된 element는 이진탐색트리의 구조를 가진다.
    def dequeue(self):        
    #-1-. 우선순위가 가장 높은 key는 최대키를 탐색하는 메소드를 활용해 구한다.                 
        x=self.findMax().key
    #-2-. 우선순위가 가장 높은 key를 delete()한다.
        self.delete(self.findMax().key)
    #-3-. value값을 반환한다.
        return x   
#4. peek() : 최대키를 탐색한 뒤 key값을 반환한다.
    def peek(self):                            
        return self.findMax().key
    def delete(self,key):
        self.root=self.delete_bst(self.root,key)
    def display(self,msg='BSTMap'):
        print(msg,end='')
        self.inorder(self.root)
        print()
    

    def search_bst(self,n,key):
        '''
        이진탐색트리 탐색연산(순환함수)
        입력: n(노드, 초기에는 루트), 찾고자하는 key 
        출력: key의 노드
        '''
        if n==None:     #찾고자 하는 key 값이 없으면
            return None     #None을 반환
        elif key==n.key:    #찾고자 하는 key 값을 찾으면
            return n        #n을 반환
        elif key<n.key:                         #찾고자 하는 key 값이 n.key보다 작으면
            return self.search_bst(n.left,key)  #재귀함수 호출후 반환된 값을 반환
        else:                                   #찾고자 하는 key 값이 n.key보다 작으면
            return self.search_bst(n.right,key) #재귀함수 호출후 반환된 값을 반환

    def search_Value_bst(self,n,key):
        if n.key==None:     #찾고자 하는 key 값이 없으면
            return None     #None을 반환
        elif key==n.key:    #찾고자 하는 key 값을 찾으면
            return n.value        #n을 반환
        elif key<n.key:                         #찾고자 하는 key 값이 n.key보다 작으면
            return self.search_Value_bst(n.left,key)  #재귀함수 호출후 반환된 값을 반환
        else:                                   #찾고자 하는 key 값이 n.key보다 작으면
            return self.search_Value_bst(n.right,key) #재귀함수 호출후 반환된 값을 반환


    def search_max_bst(self,n):
        """
        이진탐색트리 최대키 가진 노드 탐색(순환함수)
        입력: n (노드, 초기에는 루트)
        출력: n (최대키를 가진 노드)
        """
        if n!=None and n.right!=None:       # n이 루트가 아니고, 오른쪽 자식이 존재하면
            n=n.right                       #n.right는 새로운 부모노드
            return self.search_max_bst(n)   #순환된 값을 반환
        return n
    def search_min_bst(self,n):
        """
        이진탐색트리 촤소키 가진 노드 탐색(순환함수)
        입력: n (노드, 초기에는 루트)
        출력 n (최소키를 가진 노드)
        """
        if n!=None and n.left!=None:       # n이 루트가 아니고, 왼쪽 자식이 존재하면
            n=n.left                       #n.left는 새로운 부모노드
            return self.search_min_bst(n)   #순환된 값을 반환
        return n


    def insert_bst(self,r,n):
        '''
        이진탐색트리 삽입연산(노드를 삽입) (반복구조)
        입력: r(초기에는 루트노드), n(삽입할 노드)
        출력: True(삽입완료시), False(키 중복으로 삽입 실패시)
        '''
        if r == None:
            r=n
            self.root=r
            return True
        while r !=None:                          
            if n.key<r.key:                          #삽입하고자 하는 key값 r노드의 키 값보다 작으면   
                if r.left is None:                   #r노드의 좌측 자식이 없으면
                    r.left=n                         #r노드의 좌측에 삽입
                    return True
                else: 
                    r=r.left                         #r노드를 좌측 자식으로 삽입
            elif r.key<n.key:                        #삽입하고자 하는 key값 r노드의 키 값보다 크면
                if r.right is None:                  #r노드의 우측 자식이 없으면
                    r.right=n                        #r노드의 우측에 삽입
                    return True
                else:                                   #r노드의 우측에 자식이 있으면 
                    r=r.right                     #r노드를 우측 자식으로 삽입
            else:                                       #이미 key값이 존재하면 False를 반환
                return False            

    def delete_bst_case1(self,parent,node,root): #case 1 : 단말노드의 삭제
        if parent is None:          
            self.root =None
        else:
            if parent.left==node:
                parent.left=None
            else :
                parent.right=None
        return self.root
    def delete_bst_case2(self,parent,node,root): #case 2:자식이 하나인 노드 삭제
        if node.left is not None:
            child = node.left
        else:
            child= node.right
        if node==root:
            self.root=child
        else:
            if node is parent.left:
                parent.left=child
            else:
                parent.right=child
        return self.root
    def delete_bst_case3(self,parent,node,root): #case 3:자식이 2개인 노드 삭제
        succp=node      #후계자의 부모노드
        succ=node.right #후계자 노드
        while(succ.left is not None):        #후계자와 후계자 부모노드 탐색
            succp=succ
            succ=succ.left
        if (succp.left==succ):          #후계자가 왼쪽 자식이면
            succp.left=succ.right       #후계자의 오른쪽 자식을 부모노드에 연결
        else:
            succp.right=succ.right      #후게자가 오른쪽자식이면
        
        node.key=succ.key
        node.value=succ.value
        node=succ

        return self.root
    def delete_bst(self,root,key):
        if root==None: return None

        parent = None
        node = root
        while node != None and node.key!=key:
            parent=node
            if key<node.key: node =node.left
            else: node=node.right
        
        if node==None:                                      #삭제할 노드가 없을 때
            return None
        if node.left==node and node.right==None:            #case 1 단말노드
            self.root=self.delete_bst_case1(parent,node,root)
        elif node.left==None or node.right==None:            #case 2 자식이 하나인 노드
            self.root=self.delete_bst_case2(parent,node,root)
        else :                                              #case 3 자식이 2개인 노드
            self.root=self.delete_bst_case3(parent,node,root)
        return self.root
    def count_node(self,n):             #노드 개수를 구한다.
        if n is None:
            return 0
        else:
            return 1+self.count_node(n.left)+self.count_node(n.right)
    def inorder(self,n):
        if n is not None:
            self.inorder(n.left)
            print(n.key,end=' ')
            self.inorder(n.right)



map=BSTMap()
data=[35,18,7,26,12,3,68,22,30,99]

print("삽입연산 : ", data)     #우선순위 큐에 정렬되지 않은 키를 삽입한다.
for key in data :
    map.enqueue(key)
map.display("enqueue() 후 우선순위큐 : ")  

print("\n우선 순위 큐 isEmpty ? :",map.isEmpty())              #우선순위 큐가 비어있는 상태인지 확인한다.

print("\ndequeue() 반환값: ",map.dequeue())       #우선순위 큐에서 가장 우선 순위가 높은 항목을 꺼내서 반환한다.
map.display("dequeue() 후 우선순위 큐 : ")

print("\npeek() 반환값: ",map.peek())
map.display("peek() 후 우선순위 큐 : ")

print("\nsize() 반환값: ",map.size())
map.clear()
map.display("\nclear() 후 우선순위 큐 : ")




