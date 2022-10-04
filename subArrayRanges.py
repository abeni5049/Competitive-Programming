class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        iStack,dStack = [], []
        res = 0
        for i,num in enumerate(nums):
            while iStack and nums[iStack[-1]] > num:
                ind = iStack.pop()
                left = iStack[-1] if iStack else -1
                res += -nums[ind] * (ind-left) * (i-ind)
            while dStack and nums[dStack[-1]] < num:
                ind = dStack.pop()
                left = dStack[-1] if dStack else -1
                res += nums[ind] * (ind-left) * (i-ind)
            iStack.append(i)
            dStack.append(i)
        
        while iStack:
            ind = iStack.pop()
            left = iStack[-1] if iStack else -1
            res += -nums[ind] * (ind-left) * (len(nums)-ind)
        
        while dStack:
            ind = dStack.pop()
            left = dStack[-1] if dStack else -1
            res += nums[ind] * (ind-left) * (len(nums)-ind)
        
        return res
