class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jd = jobDifficulty
        n = len(jd)
        if n < d: return -1
        @lru_cache(None)
        def dp(i,day):
            if day == 1: return max(jd[i:])
            res,max_jd = float('inf'),0
            for j in range(i,n-day+1):
                max_jd = max(max_jd,jd[j])
                res = min(res,max_jd+dp(j+1,day-1))
            return res
        return dp(0,d)
