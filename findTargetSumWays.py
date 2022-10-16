class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i,sum_):
            if i == -1: return  1 if sum_ == target else 0
            return dfs(i-1,sum_+nums[i]) + dfs(i-1,sum_-nums[i])
        
        return dfs(len(nums)-1,0)
