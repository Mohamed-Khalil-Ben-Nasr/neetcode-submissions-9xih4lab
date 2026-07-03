class QueueNode:
    def __init__(self):
        self.val = -1
        self.nxt = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = QueueNode()
        self.tail = QueueNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = QueueNode()
        newNode.val = value
        newNode.nxt = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.nxt = newNode
        self.tail.prev = newNode 
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.nxt = self.head.nxt.nxt
        self.head.nxt.prev = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.head.nxt.val
        

    def Rear(self) -> int:
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()