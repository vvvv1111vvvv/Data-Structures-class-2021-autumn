# 연결된 구조  : 스택


class Node:     #단순연결을 위한 노드 
    def __init__(self,elem,link=None):      #생성자 디폴트 인수 사용
        self.data = elem                    #데이터 멤버 생성 및 초기화
        self.link= link                     #링크 생성 및 초기화

class LinkedStack:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        return self.top==None
    def clear(self):
        self.top=None
    def push(self, item):           #여기서 링크 연결이 생긴다.
        n=Node(item,self.top)
        self.top=n
    def pop(self):                  
        if not self.isEmpty():
            data = self.top.data
            self.top=self.top.link
            return data
    def peek(self):
        if not self.isEmpty:
            return self.top.data
    def size(self):
        n=self.top
        count=0
        while not n == None:
            n=n.link
            count+=1
        return count
    def display(self, msg='LinkedStack:'):
        print(msg, end="")
        node = self.top
        while not node == None:
            print(node.data)
            node=node.link
        print()
odd=LinkedStack()
even=LinkedStack()
for i in range (10):
    if i%2==0:
        even.push(i)
    else:
        odd.push(i)
odd.display()
even.display()
odd.pop()
odd.pop()
even.pop()
odd.display()
even.display()