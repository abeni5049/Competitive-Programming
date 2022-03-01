

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None        

    def get(self, index: int) -> int:
        if not self.head: return -1
        count = 0
        curr =  self.head
        while curr and count<index:
            count += 1
            curr = curr.next
        return curr.val if count == index and curr else -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        prevHead = self.head 
        self.head = Node(val)
        self.head.next = prevHead

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next 
        prev.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        count = 0
        while curr and count < index:
            prev = curr
            curr = curr.next
            count += 1
        if count == index:
            newNode = Node(val)
            if curr == self.head:
                newNode.next = curr
                self.head = newNode
            else:   
                newNode.next = prev.next
                prev.next = newNode
                
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        count = 0
        while curr and count < index:
            prev = curr
            curr = curr.next
            count += 1
        if count == index and curr:
            if curr == self.head:
                self.head = self.head.next
            else:
                prev.next = curr.next
                

        
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
