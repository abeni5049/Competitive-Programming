# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1: return None
        return self.divide(lists,0,len(lists)-1)

    def divide(self,lists,l,r):
        if l == r: return lists[l]
        mid = (l+r) // 2
        l = self.divide(lists,l,mid)
        r = self.divide(lists,mid+1,r)
        return self.merge(l,r)

    def merge(self,head1,head2):
        if not head1:
            return head2
        if not head2:
            return head1
        curr1 = head1
        curr2 = head2
        if head1.val < head2.val:
            head = head1
            curr1 = curr1.next
        else:
            head = head2
            curr2 = curr2.next
            
        merged = head
        while curr1 and curr2:
            if curr1.val < curr2.val:
                merged.next = curr1
                merged = curr1
                curr1  = curr1.next
            else:
                merged.next = curr2
                merged = curr2
                curr2 = curr2.next
        
        while curr1:
            merged.next = curr1
            merged = curr1
            curr1  = curr1.next
        while curr2:
            merged.next = curr2
            merged = curr2
            curr2 = curr2.next
        return head
    
