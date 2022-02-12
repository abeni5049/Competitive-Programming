# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
            
        mid = count//2
        curr = head
        count = 0
        while count < mid:
            curr = curr.next
            count += 1
        return curr
