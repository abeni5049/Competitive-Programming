# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        #convert linked list to array
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        #sort the array
        arr.sort()
        
        #convert array back to linked list
        head = ListNode(arr[0])
        curr = head
        for i in range(1,len(arr)):
            newNode = ListNode(arr[i])
            curr.next = newNode
            curr = newNode
        return head
        
