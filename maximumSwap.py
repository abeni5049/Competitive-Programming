class Solution:
    def maximumSwap(self, nums: int) -> int:
        nums = list(str(nums))
        sorted_nums = sorted(nums,reverse=True)
        index = 0
        for i, digit in enumerate(nums):
            if int(digit) != int(sorted_nums[i]):
                index = i
                break
        desIndex = 0
        for i, num in enumerate(nums):
            if num == sorted_nums[index]:
                desIndex = i
        nums[index], nums[desIndex] = nums[desIndex], nums[index]
        return int(''.join(nums))
