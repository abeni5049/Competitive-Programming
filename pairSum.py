# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        first find middle node using slow and fast pointers
        reverse from middle to last 
        ith element of original linked list is twin with ith node of reversed linkedlist
        compare the sum of current twin with prev twin and store the max
        return the max sum
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        res = -1
        originalList = head
        reversedList = prev
        while originalList and reversedList:
            currSum = originalList.val + reversedList.val
            res = max(res,currSum)
            originalList = originalList.next
            reversedList = reversedList.next
        return res
        
        
        
