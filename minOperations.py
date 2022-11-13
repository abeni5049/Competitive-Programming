class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        GCD_of_all_num = gcd(*numsDivide)
        min_deletions = 0
        heapify(nums)
        while nums:
            num = heappop(nums)
            if GCD_of_all_num % num == 0: return min_deletions
            if num > GCD_of_all_num: return -1
            min_deletions += 1
        return -1
