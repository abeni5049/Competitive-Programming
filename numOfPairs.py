class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            for j in range(N):
                if i != j and nums[i]+nums[j] == target:
                    count += 1
        return count
