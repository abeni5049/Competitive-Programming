# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        #convet linked list to array
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        #sort the array using merge sort
        arr = self.msort(arr,0,len(arr)-1)
        
        #convert array back to linked list
        head = ListNode(arr[0])
        curr = head
        for i in range(1,len(arr)):
            newNode = ListNode(arr[i])
            curr.next = newNode
            curr = newNode
        return head
        
    def msort(self,arr,start,end):
        if start == end : return [arr[start]]
        mid = (start + end)//2
        l = self.msort(arr,start,mid)
        r = self.msort(arr,mid+1,end)
        return self.merge(l,r)
    
    def merge(self,arr1 , arr2):
        i = 0
        j = 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        return res
   
