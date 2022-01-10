class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq=total=left=right=0
        for right in range(len(nums)):
            total += nums[right]
            while nums[right] * (right-left+1) > total + k:
                total -= nums[left]
                left += 1
            maxFreq = max(maxFreq,(right-left+1))   
        return maxFreq
    
    
