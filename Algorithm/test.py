from collections import deque

queue = deque()


def queue_pop():
    del queue[0]

def queue_push(data):
    queue.append(data)


queue_push(5)
queue_push(2)
queue_push(3)
queue_push(7)
queue_pop()
queue_push(1)
queue_push(4)
queue_pop()

queue.reverse()
a = list(queue)

print(a)