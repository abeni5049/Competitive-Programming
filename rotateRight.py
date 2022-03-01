# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        #count the number of nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k = k % n
        if k == 0 : return head

        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr = last = prev
        prev = None
        count = 0
        while curr and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        head = prev
        
        
        prev = None
        count = 0
        while curr and count < n-k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        last.next = prev
        
        return head
