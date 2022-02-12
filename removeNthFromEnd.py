# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list = []
        curr = head
        while curr:
            list.append(curr)
            curr = curr.next
                  
        if len(list) == n:
            head = head.next
            return head
        
        list[-n-1].next = list[-n-1].next.next
        
        return head
