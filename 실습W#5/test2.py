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


a=CircularQueue()
for i in range (6):
    a.enqueue(i)
a.display()
print(a.items)

#원형 큐





