# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(0,head)
        last,prev,curr = dummy, head,head.next
        value = float("-inf")
        while prev and curr:
            if prev.val == curr.val:
                value = curr.val
                last.next = curr.next
                prev = curr.next
                curr = curr.next.next if curr.next else None
            elif value == prev.val:
                value = prev.val
                last.next = curr
                prev,curr = curr,curr.next 
            else:
                value = prev.val
                last,prev,curr = prev,curr,curr.next
        if prev and value == prev.val: last.next = prev.next 
        return dummy.next
                    
