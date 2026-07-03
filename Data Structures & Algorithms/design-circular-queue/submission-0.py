class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.capacity = k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        # queue full
        if self.capacity == 0:
            return False
        # queue empty
        if self.capacity == len(self.q):
            # this element should be both the head and tail
            self.q[self.head] = value
        # queue already has >= 1 elements
        else:
            # handle wrap around
            self.tail = (self.tail + 1) % len(self.q)
            # insert new element at the end of the queue
            self.q[self.tail] = value

        # update capacity
        self.capacity -= 1

        # success
        return True

    def deQueue(self) -> bool:
        # if q empty
        if self.capacity == len(self.q):
            return False
        
        # if there is only one element in the queue
        # => delete it by overwriting the value with -1
        # => dont update pointers
        if self.head == self.tail and self.capacity == len(self.q)-1:
            self.q[self.head] = -1
        else:
            # pop the first element in the queue by updating head
            # handle wrap around
            self.head = (self.head + 1) % len(self.q)

        # update capacity
        self.capacity += 1

        # success
        return True  

    def Front(self) -> int:
        return self.q[self.head]
        

    def Rear(self) -> int:
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.capacity == len(self.q)

    def isFull(self) -> bool:
        return self.capacity == 0
    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()