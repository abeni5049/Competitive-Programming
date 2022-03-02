class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0
        for i,num in enumerate(nums):
            rsum -= num
            if lsum == rsum:
                return i
            lsum += num
        return -1
