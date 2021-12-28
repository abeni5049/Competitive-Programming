class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        for i in range(len(nums)//2):
            pairs.append([nums[i],nums[-(i+1)]])
        pairs.sort(key=lambda x:x[0]+x[1])
        print(pairs)
        return pairs[-1][0] + pairs[-1][1]