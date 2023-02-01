class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        nums = [(ages[i],scores[i]) for i in range(len(ages))]
        nums.sort()
        dp = [nums[i][1] for i in range(len(ages))]
        for i in range(len(ages)):
            for j in range(i):
                if nums[j][1] <= nums[i][1] or nums[i][0] == nums[j][0]:
                    dp[i] = max(dp[i],dp[j]+nums[i][1])
        return max(dp)
