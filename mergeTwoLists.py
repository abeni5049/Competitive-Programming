class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2: return list2
        if not list2 and list1: return list1
        if not list1 and not list2: return None
        l1 = list1
        l2 = list2
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        merged = head
        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                merged = l1
                l1 = l1.next
            else:
                merged.next = l2
                merged = l2
                l2 = l2.next
        while l1:
            merged.next = l1
            merged = l1
            l1 = l1.next
        while l2:
            merged.next = l2
            merged = l2
            l2 = l2.next
        return head
