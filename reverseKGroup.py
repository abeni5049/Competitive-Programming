# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        num = 0
        curr = head
        while curr:
            curr = curr.next
            num += 1
        def reverse(head,count,num):
            if not head: return head
            if num - count < k: return head
            m = 0
            node = head
            while m < k:
                node = node.next
                m += 1
            temp = head.next
            head.next = reverse(node,(count+k),num)
            prev = head
            curr = temp
            n = 2
            while curr and n <= k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                n += 1
            return prev
        return reverse(head,0,num)
