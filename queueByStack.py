class MyQueue:
    stack1 = []
    def __init__(self):
        self.stack1.clear()
    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int: 
        if not self.stack1:
            return -1
        front = self.stack1[0]
        del self.stack1[0]
        return front

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        if not self.stack1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
