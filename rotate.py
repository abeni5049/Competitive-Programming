class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """   
        k = k % len(nums)
        nums[:] = self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        nums[k:] = self.reverse(nums[k:])
        
    def reverse(self,arr):
        l = 0
        r = len(arr) - 1
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
        return arr
        
