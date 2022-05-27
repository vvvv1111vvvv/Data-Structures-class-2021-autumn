max_qsize=20
class CircularQueue():
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[None]*max_qsize
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front == (self.rear+1)%max_qsize
    def clear(self):
        self.front=self.rear
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1) % max_qsize
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%max_qsize
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%max_qsize]
    def size(self):
        return (self.rear- self.front+max_qsize)%max_qsize
    def display(self):
        out=[]
        if self.front < self.rear:
            out=self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:max_qsize]\
                + self.items[0:self.rear+1]
        print(out)

def isValidPos(x,y,maze_size=6):
    if x<0 or y<0 or x>=maze_size or y>=maze_size:
        return False
    else: 
        return map[y][x]=='0' or map[y][x]=='x'

def BFS():
    que=CircularQueue()
    que.enqueue((0,1))
    print("BFS")

    while not que.isEmpty():
        here=que.dequeue()
        print(here,end='-->')
        x,y= here  
        if map[y][x]=='x':
            return True
        else:
            map[y][x]='.'
            if isValidPos(x+1,y): que.enqueue((x+1,y)) # 우
            if isValidPos(x-1,y): que.enqueue((x-1,y)) # 좌
            if isValidPos(x,y+1): que.enqueue((x,y+1)) # 상
            if isValidPos(x,y-1): que.enqueue((x,y-1)) # 하

    return False





map=[['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']]
maze_size=6
result=BFS()
if result :print(" --> 미로탐색 성공")
else : print(' --> 미로탐색 실패')