class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        freq = {0:1}
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ - k in freq:
                res += freq[sum_-k]
            if sum_ in freq:
                freq[sum_] += 1
            else: 
                freq[sum_] = 1
            freq[sum_] = freq.get(sum_,0)
        return res
