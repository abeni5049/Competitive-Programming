class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [-1]*len(nums)
        j = len(nums)//2
        for i in range(0,len(nums),2):
            result[i] = nums[j]
            j += 1
        index = 0
        for i in range(1,len(nums),2):
            result[i] = nums[index]
            index += 1
        return result
            
