# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        num1 = ''
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        
        curr2 = l2
        num2 = ''
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next
            
        sum_ = int(num1[::-1]) + int(num2[::-1])
        sum_ = str(sum_)[::-1]
        head = ListNode(sum_[0])
        prev = head
        for i in range(1,len(sum_)):
            curr = ListNode(sum_[i])
            prev.next = curr
            prev = curr
        return head
