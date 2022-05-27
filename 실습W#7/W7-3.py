'''
작성자 : vvvv1111vvvv
작성일 : 2021.10.21

1. 목적: 정렬을 활용하는 방법에 대해 실습한다.
2. 문제 : 7.3절의 합집합 코드를 참조하여 정렬된 리스트를 사용해 효율적인 교집합 함수를 구현

3. 방법 : 7.3절의 합집합 코드를 사용한다.

알고리즘:
#1. 집합클래스의 객체 s와 t를 선언한다.
#2. s와 t에 정렬된 리스트를 insert()한다.
#3. 입력된 리스트에 intersection() 를 사용한다.
#4. 반환된 결과를 출력한다.
'''

class SetByArrayList():
    def __init__(self):
        self.item=[]
    def insert(self,item):
        if item in self.item:
            return
        for idx in range (len(self.item)):
            if item<self.item[idx]:
                self.item.insert(idx,item)
                return

        self.item.append(item)
        return

    def __eq__(self,setB):
        if self.size()!=setB.size():
            return False
        for i in range (len(self.item())):
            if self.item[i]!=setB.item[i]:
                return False
        return True
    def size(self):
        return len(self.item())
    def intersection(self,setB):
        newset= SetByArrayList()
        a=0
        b=0
        while a<len(self.item) and b<len(setB.item):
            ValueA=self.item[a]
            ValueB=setB.item[b]
            if ValueA<ValueB:
                a+=1
            elif ValueA>ValueB:
                b+=1
            elif ValueA==ValueB:
                newset.item.append(ValueA)
                a+=1
                b+=1
        return newset
#1. 집합클래스의 객체 s와 t를 선언한다.

s=SetByArrayList()
t=SetByArrayList()

#2. s와 t에 정렬된 리스트를 insert()한다.
s.insert(1)
s.insert(11)
s.insert(26)
s.insert(35)
s.insert(39)
s.insert(40)

t.insert(1)
t.insert(17)
t.insert(26)
t.insert(34)
t.insert(35)
t.insert(36)
t.insert(37)
#3. 입력된 리스트에 intersection() 를 사용한다.
#4. 반환된 결과를 출력한다.
print(s.intersection(t).item)
