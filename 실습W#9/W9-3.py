'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.11

1. 목적: 이진탐색트리의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 9.3: 이진탐색트리를 중위순회하면 정렬된 숫자를 얻을 수 있다.
                    이를 이용하여 다음 배열에 들어 있는 숫자들을 정렬시키는 함수를 작성하여보라
                    배열에 들어있는 숫자들을 이진탐색트리에 축한후 트리를 중위 순회하면서 숫자들을 출력한다.
3. 방법 : 9.2절의 함수와 테스트 코드를 응용한다.

알고리즘
#1. 배열을 정의한다.
#2. 정렬 전 배열을 출력
#3. 배열에 들어있는 숫자들은 이진탐색트리에 추가
#4. 정렬 후 배열을 출력
'''




class BSTNode():                #이진탐색트리를 위한 노드클래스
    def __init__(self,key, value):
        self.key=key        #key값
        self.value=value    #value값
        self.left=None      #왼쪽자식에 대한 링크
        self.right=None     #우측자식에 대한 링크


class BinarySearchTree():       #이진탐색트리를 위한 트리 클래스
    def __init__(self):             #생성자 : 초기에 root는 비어있다.
        self.root=None

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
    def inorder(self,n):
        if n is not None:
            self.inorder(n.left)
            print(n.key,end=' ')
            self.inorder(n.right)


a=BinarySearchTree()

#1. 배열을 정의한다.
inputList=[11,3,4,1,56,5,6,2,98,32,23]

#2.정렬 전 배열을 출력
print("정렬 전: ",inputList)

#3. 배열에 들어있는 숫자들은 이진탐색트리에 추가
for i in inputList:        
    a.insert_bst(a.root,BSTNode(i,'0'))

#4. 정렬 후 배열을 출력
print("정렬 후: ",end='')
a.inorder(a.root)        
