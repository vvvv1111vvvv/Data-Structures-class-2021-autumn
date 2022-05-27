class queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def enqueue(self, item):
        self.items.append(item)    
    def dequeue(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]

a=queue()
for i in range(2,8,+2):
    a.enqueue(i)

print(a.items)

#선형큐