# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        prev = head
        cur = head.next
        while prev and cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
