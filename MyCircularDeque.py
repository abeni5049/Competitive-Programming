class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if not self.deque:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return True if not self.deque else False

    def isFull(self) -> bool:
        return True if len(self.deque) == self.deque.maxlen else False
            


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
