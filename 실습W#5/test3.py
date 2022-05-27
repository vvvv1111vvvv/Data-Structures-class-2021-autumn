import queue #파이썬 큐 모듈 포함

Q=queue.Queue(maxsize=20)
for v in range(1,10):
    Q.put(v)                #enqueue대체
print('Q의 내용 : ',end='')
for _ in range (1, 10):
    print(Q.get(), end=' ') # dequeue 대체
print()