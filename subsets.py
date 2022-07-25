class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,arr):
            res.append(arr)
            for j in range(i,len(nums)):
                dfs(j+1,arr+[nums[j]])
        dfs(0,[])
        return res
