class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()  
        count=0 
        for i in range(1,len(nums)):
            if nums[i]<= nums[i-1]:
                val=nums[i-1]-nums[i]+1
                count+=val
                nums[i]+=val
        return count
