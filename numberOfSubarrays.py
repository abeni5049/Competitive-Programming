class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0:1}
        sum_ = 0
        for num in nums:
            sum_ += 1 if num % 2 else 0
            res += prefix.get(sum_-k,0)
            prefix[sum_] = 1 + prefix.get(sum_,0)
        return res
            
