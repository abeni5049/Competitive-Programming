class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        max_ = 0
        temp = k
        while r < len(nums):
            if temp < 0:
                if nums[l] == 0:
                    temp += 1
                l += 1
            else:
                if nums[r] == 0: 
                    temp -= 1
                if temp >= 0:
                    max_ = max(max_,r-l+1)
                r += 1
        return max_
            
