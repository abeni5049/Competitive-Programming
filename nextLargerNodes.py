# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        res = [0] * len(arr)
        mstack = []
        for i,num in enumerate(arr):
            while mstack and num > arr[mstack[-1]]:
                res[mstack.pop()] = num
            mstack.append(i)
        return res
