class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(sum_):
            if target == sum_: return 1
            if sum_  in memo: return memo[sum_]
            res = 0
            for num in nums:
                if target >= sum_+num:
                    res += dfs(sum_+num)
            memo[sum_] = res
            return res
        return dfs(0)
