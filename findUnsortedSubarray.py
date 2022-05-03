class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        start = end = 0
        for i,num in enumerate(nums):
            if num != arr[i]: 
                start = i
                break
        for j,num in enumerate(nums[::-1]):
            if num != arr[-j-1]: 
                end = len(nums) - j
                break
        return end - start
        
