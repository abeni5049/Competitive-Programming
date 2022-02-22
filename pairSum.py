# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        res = -1
        for i in range(len(arr)//2):
            currSum = arr[i] + arr[len(arr)-1-i]
            res = max(res,currSum)
        return res
