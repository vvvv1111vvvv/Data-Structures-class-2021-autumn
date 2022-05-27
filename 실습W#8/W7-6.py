'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.04

1. 목적: 탐색을 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 7.6 : 7.7절에서 구현한 해시 맵을 수정하여 선형조사법을 이용한 해시 맵으로 구현하라

3. 방법 : 7.5절에서 구현한 해시 맵을 수정하여
          선형조사법의 삽입, 탐색, 삭제 연산을 해시 맵으로 구현한다.

알고리즘:
#1. 삽입연산 : key 값을 hashFn()함수로 헤싱한다.
                이 값을 idx에 저장한다. 만약 idx값이 None 또는 Removed 라면 엔트리 key와 value값을 참조한다.
                만약 idx가 차있을 경우 한칸씩 우측으로 움직이며 빈공간을 찾아 삽입한다.
#2. 삭제연산 :   search()를 통해 만약 찾고자 하는 key값이 존재 HashMap에 존재하지 않으면 리턴한다.
                존재할경우 해당 HashMap에 'Removed'를 삽입한다.

#3. 탐색연산 :  key 값을 hashFn()함수로 헤싱한다.
                만약 헤싱한 idx값의 Entry의 key가 찾고자 하는 key와 동일하다면 idx 값을 반환한다.
                만약 다를 경우 idx 값을 증가시켜 가며 동일한 key가 존재하는지 확인한다.
                한바퀴를 다 돌았을 때, 동일한 key가 존재하지 않는다면 None을 반환한다.
'''
class Entry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))

class HashMap:         #헤시맵
    def __init__(self,M):
        self.table=[None]*M
        self.M=M
    def hashFn(self,key):
        sum=0
        for c in key:
            sum=sum+ord(c)
        return sum%self.M
    def insert(self,key,value):
        idx=self.hashFn(key)        #해시주소계산
        for j in range (self.M):
            if self.table[idx]==None or self.table[idx]=='Removed':
                self.table[idx]=Entry(key,value)
                return
            else:
                idx=idx+1
                if idx==self.M:
                    idx=0
        print("HashMap이 가득 차 있습니다.")
        return None
    def search(self,key):
        idx=self.hashFn(key)
        for i in range (self.M):
            if self.table[idx].key==key:
                return idx
            idx+=1
            if idx==self.M:
                idx=0
        print("찾고자하는 key가 존재하지 않습니다.")
        return None

    def delete(self,key):
        if self.search(key)==None:

            return
        idx=self.search(key)
        self.table[idx]='Removed'

    def display(self,msg):
        print(msg)
        for entry in self.table:
            if entry is not None:
                print(" ",entry)

map=HashMap(40)
map.insert('data','자료')
map.insert('sturcture','구조')
map.insert('Binary search','이진탐색')
map.insert('gamer','게이머')
map.insert('remag','머이게')
map.insert('arrary','정렬')
map.display('나만의 단어장 : ')

print('탐색 :gamer -->', map.search('gamer'))
print('탐색 :remag -->', map.search('remag'))
print('탐색: arrary -->', map.search("arrary"))
print("탐색: sturcture-->", map.search('sturcture'))

map.delete("arrary")
map.display("나만의 단어장:")
