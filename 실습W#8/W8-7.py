'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.11

1. 목적: 트리의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 8.7:  배열로 표현된 완전이진트리 A가 힙 조건을 만족하는지를 검사하는 다음 함수를 순환적인
        방법을 구현하고 테스트하라, 다음 함수 들을 구현하여야 한다.
3. 방법 : 8.5절의 함수와 테스트 코드를 응용한다.

알고리즘
#1. 완전이진트리를 배열로 구현한다. class completeBinaryTree()
#2. Min 힙 여부를 확인하는 메소드 isMinHeapRecur(id)
    순환적으로 구현한다.
    -1-.터미널이면 True를 반환 (id값이 이진트리의 크기 보다 클 때)
    -2-.Left만 존재할 때, Left 의 값이 Parent보다 크면, Left의 id값을 재귀한 결과를 반환
    -3-.Left와 Right가 Parent보다 크면, 각각 id값을 재귀한뒤 and 값을 반환
    -4-. 만약 Left 와 Right 중 어느 하나라도, Parent보다 작다면, false를 반환

#3. Max 힙 여부를 확인하는 메소드 isMaxHeapRecur(id)
    -1-.터미널이면 True를 반환 (id값이 이진트리의 크기 보다 클 때)
    -2-.Left만 존재할 때, Left 의 값이 Parent보다 작으면, Left의 id값을 재귀한 결과를 반환
    -3-.Left와 Right가 Parent보다 작다면, 각각 id값을 재귀한뒤 and 값을 반환
    -4-. 만약 Left 와 Right 중 어느 하나라도, Parent보다 크면, false를 반환
#4. 결과를 출력한다.
'''

#1. 완전이진트리를 배열로 구현한다. class completeBinaryTree()
class completeBinaryTree:
    def __init__(self):
        self.bitree=[]
        self.bitree.append(0)
    def size(self):
        return len(self.bitree)-1
    def isEmpty(self):
        return self.size()==0
    def Parent(self,i):
        return self.bitree[i//2]
    def Left(self,i):
        return self.bitree[i*2]
    def Right(self,i):
        return self.bitree[i*2+1]
    def display(self,msg='이진 트리'):
        print(msg,self.bitree[1:])
    def insert(self,n):
        self.bitree.append(n)
    def delete(self):
        if not self.isEmpty():
            top=self.bitree.pop(1)
            return top
    def isMinHeapRecur(self,id):        #순환적
    #2. Min 힙 여부를 확인하는 메소드 isMinHeapRecur(id)
        if (id*2)>self.size():                  #    -1-.터미널이면 True를 반환 (id값이 이진트리의 크기 보다 클 때)
            print("case : 1 -> ", end='')
            return True
        elif self.Left(id)>=self.bitree[id] and (id*2+1)>self.size():   #-2-.Left만 존재할 때, Left 의 값이 Parent보다 크면, Left의 id값을 재귀한 결과를 반환
            print("case : 2 -> ", end='')
            return self.isMinHeapRecur(id*2)
        elif self.Left(id)>=self.bitree[id] and self.Right(id)>=self.bitree[id]:    #-3-.Left와 Right가 Parent보다 크면, 각각 id값을 재귀한뒤 and 값을 반환
            print("case : 3 -> ", end='')
            m=self.isMinHeapRecur(id*2)
            n=self.isMinHeapRecur(id*2+1)
            return m and n
        elif self.Left(id)<self.bitree[id] or self.Right(id)<self.bitree[id]:       #-4-. 만약 Left 와 Right 중 어느 하나라도, Parent보다 작다면, false를 반환
            print("case : 4 -> ", end='')
            return False
    def isMaxHeapRecur(self,id):        #순환적
    #3. Max 힙 여부를 확인하는 메소드 isMaxHeapRecur(id)
        if (id*2)>self.size():                 # -1-.터미널이면 True를 반환 (id값이 이진트리의 크기 보다 클 때)
            print("case : 1 -> ", end='')
            return True
        elif self.Left(id)<=self.bitree[id] and (id*2+1)>self.size():       # -2-.Left만 존재할 때, Left 의 값이 Parent보다 작으면, Left의 id값을 재귀한 결과를 반환
            print("case : 2 -> ", end='')
            return self.isMaxHeapRecur(id*2)
        elif self.Left(id)<=self.bitree[id] and self.Right(id)<=self.bitree[id]:    #    -3-.Left와 Right가 Parent보다 작다면, 각각 id값을 재귀한뒤 and 값을 반환
            print("case : 3 -> ", end='')
            m=self.isMaxHeapRecur(id*2)
            n=self.isMaxHeapRecur(id*2+1)
            return m and n
        elif self.Left(id)>self.bitree[id] or self.Right(id)>self.bitree[id]:       #    -4-. 만약 Left 와 Right 중 어느 하나라도, Parent보다 크면, false를 반환
            print("case : 4 -> ", end='')
            return False

a=completeBinaryTree()
b=completeBinaryTree()
c=completeBinaryTree()

data1=[2,5,4,8,9,3,7,3]
data2=[1,4,2,7,5,3,3,7,8,9]
data3=[9,7,6,5,4,3,2,2,1,3]

print("삽입연산: ",data1)
for elem in data1:
    a.insert(elem)
print("삽입연산: ",data2)
for elem in data2:
    b.insert(elem)
print("삽입연산: ",data3)
for elem in data3:
    c.insert(elem)
a.display("a 삽입 후: ")
b.display("b 삽입 후: ")
c.display("c 삽입 후: ")

#4. 결과를 출력한다.
print("a : isMinHeap ? :")
print(a.isMinHeapRecur(1))
print("b : isMinHeap ? :")
print(b.isMinHeapRecur(1))
print("c : isMinHeap ? :")
print(c.isMinHeapRecur(1),"\n\n")

print("a : isMaxHeap ? :")
print(a.isMaxHeapRecur(1))
print("b : isMaxHeap ? :")
print(b.isMaxHeapRecur(1))
print("c : isMaxHeap ? :")
print(c.isMaxHeapRecur(1))
