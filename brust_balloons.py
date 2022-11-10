class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n) ]
        for width in range(2,n):
            for l in range(n-width):
                r = l+width
                max_coins = float('-inf')
                for k in range(l+1,r):
                    coins = nums[l] * nums[k] * nums[r]
                    max_coins = max(max_coins,coins+dp[l][k]+dp[k][r])
                dp[l][r] = max_coins 
        return dp[0][n-1]
                    
