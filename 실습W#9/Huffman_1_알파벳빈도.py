'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.11

1. 목적: 힙과 허프만코드를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : Huffman_1: 문서의 알파벳 빈도를 찾는 프로그램을 작성한다.
3. 방법 : 8.6절의 함수와 테스트 코드를 응용한다.

'''
class MinHeap :
    def __init__ (self) :
        self.heap = []
        self.heap.append(0)

    def size(self) : return len(self.heap) - 1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '힙 트리: ') :
        print(msg, self.heap[1:])

    def insert(self, n) :
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n < self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self) :
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child += 1
                if last <= self.heap[child] :
                    break;
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot



def bringText():
    frequency=[0]*52
    filename = input("경로를 입력하시오") #원하는 파일의 경로를 입력/ 주의사항; 경로에서 역슬레쉬 대신 슬래쉬 사용
    file = open(filename , "r" ,encoding='utf-8') #읽기전용, 유니코드인코딩
    data = file.read()      #파일의 모든 내용 읽음
    file.close()            #파일 닫기
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    j=0
    for elem in data:          #읽은 각 문자에 대헤
        for i in alphabet:
            if i==elem:
                frequency[j]+=1
                break
            j+=1
        j=0
    j=0
    for i in alphabet:
        print(i, " : ", frequency[j])
        j+=1
    return frequency
def make_tree(freq):
    for n in freq:
        heap.insert(n)
    for i in range (0,51):
        e1=heap.delete()
        e2=heap.delete()
        heap.insert(e1+e2)
        print("(%d+%d)"%(e1,e2))


heap = MinHeap()
make_tree(bringText())
heap.display()
