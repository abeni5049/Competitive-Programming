# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.        
        """
        """
        First get the middle element by slow and fast pointers
        unattach the node before middle from middle node
        reverse the linked list form mid to end
        merge the two linked list (by that pattern)   
        """
        #get the middle node
        last = slow = fast = head
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
            
        #unattach element before middle (to prevent cycle)
        last.next = None
        
        #reverse linked list(mid - end)
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        #merge two linked lists
        oriNode = head
        midNode = prev
        while oriNode and midNode:
            temp = oriNode.next
            temp2 = midNode.next
            oriNode.next = midNode
            midNode.next = temp
            last = midNode
            oriNode = temp
            midNode = temp2
            
        if midNode:
            last.next = midNode
            
            
