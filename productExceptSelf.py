class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        prefix = 1
        for num in nums:
            res.append(prefix)
            prefix *= num
            
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
