'''
작성자 : vvvv1111vvvv

1. 목적: 정렬을 활용하는 방법에 대해 실습한다.
2. 문제 : 3.3절의 배열로 구현한 리스트 클래스 ArrayList에서 리스트 항목의 정렬을 위해 sort()메소드를 사용하였다.
            이것을 사용하지 않고 정렬 알고리즘을 이용해 ArrayList의 sort()를 다시 구현하라, 정렬 알고리즘으로는 삽입정렬을 사용

3. 방법 : 삽입정렬 알고리즘을 사용하여 주어진 리스트를 정렬한다.

알고리즘:
#1. ArrayList의 객체 a를 선언한뒤 수를 입력한다.
#2. ArraryList클래스의 sort() 함수를 호출한다.
#3. 입력된 리스트를 삽입정렬 알고리즘을 이용해 정렬한다.
#4. 반환된 결과를 출력한다.
'''




class ArrayList():
    def __init__(self):
        self.item=[]
    def insert(self,pos,item):
        self.item.append(item)
        for i in range(len(self.item)-pos):
            self.item.append(self.item.pop(pos))
    def delete(self,pos):
        b=[]
        for i in range (len(self.item)-pos-1):
            b.append(self.item.pop(-1))
        x=self.item.pop(-1)
        for i in range (len(b)):
            self.item.append(b[i])
        return x
    def isEmpty(self):
        return len(self.item)==0
    def getEntry(self, pos):
        return self.item[pos]
    def find(self,item):
        return self.item.index(item)
    def replace(self, pos, item):
        self.insert(pos,item)
        self.item.pop(pos+1)
    def display(self):
        print(self.item)
#3. 입력된 리스트를 삽입정렬 알고리즘을 이용해 정렬한다.
    def sort(self):
        for i in range(1,len(self.item)):
            j=i-1
            key=self.item[i]
            while j>-1 and self.item[j] > key:
                self.item[j+1]=self.item[j]
                j=j-1
            self.item[j+1]=key




#1. ArrayList의 객체 a를 선언한뒤 수를 입력한다.

a=ArrayList()

a.insert(3,4)
a.insert(2,42224)
a.insert(0,444)
a.insert(2,17)
a.insert(2,2)
print(a.item)
a.delete(2)
print(a.item)
#2. ArraryList클래스의 sort() 함수를 호출한다.
a.sort()
#4. 반환된 결과를 출력한다.
a.display()
