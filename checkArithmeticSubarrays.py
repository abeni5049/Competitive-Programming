class Solution:
    def checkArt(self,nums):
        nums.sort()
        dif = nums[1] - nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] != dif:
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            result.append(self.checkArt(nums[l[i]:r[i]+1]))
        return result