class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 0
        for num in nums:
            if num-1 not in nums:
                curr = num+1
                while curr in nums:
                    curr = curr + 1
                longest_sequence = max(longest_sequence,curr-num)
        return longest_sequence
            
