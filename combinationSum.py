class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i,sum_,arr):
            if sum_ == target:
                res.append(arr)
                return 
            for j in range(i,len(candidates)):
                if sum_ + candidates[j] > target: break
                dfs(j,sum_+candidates[j],arr+[candidates[j]])
        dfs(0,0,[])
        return res
