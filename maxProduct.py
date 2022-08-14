class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = max_ = res = nums[0]
        for i in range(1,len(nums)):
            temp = min(min_*nums[i],max_*nums[i],nums[i])
            max_ = max(min_*nums[i],max_*nums[i],nums[i])
            res = max(res,max_)
            min_ = temp
        return res
