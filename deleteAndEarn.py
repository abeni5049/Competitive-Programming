class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(freq.keys())
        lookup = {}
        def dp(i):
            if i in lookup: return lookup[i]
            if i < 0: return 0
            if nums[i-1] == nums[i]-1:
                takeit = dp(i-2) + nums[i]*freq[nums[i]]
                dont_takeit = dp(i-1)
            else:
                takeit = dp(i-1) + nums[i]*freq[nums[i]]
                dont_takeit = dp(i-1)        
            lookup[i] = max(takeit,dont_takeit)
            return lookup[i]
        return dp(len(nums)-1)
        
