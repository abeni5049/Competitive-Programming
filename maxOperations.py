class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        result = 0
        for key in freq:
            if k - key in freq:
                result += min(freq[key],freq[k-key])
                    
        return result//2