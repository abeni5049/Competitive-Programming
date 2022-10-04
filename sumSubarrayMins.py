class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9+7
        res = 0
        mstack = []
        for i,num in enumerate(arr):
            while mstack and arr[mstack[-1]] >= num:
                ind = mstack.pop()
                left = mstack[-1] if mstack else -1
                res += arr[ind] * (i-ind) * (ind-left if ind != left else 1)
            mstack.append(i)
        
        while len(mstack)>1:
            ind = mstack.pop()
            res += arr[ind] * (len(arr)-ind) * (ind-mstack[-1])
            
        if mstack:
            ind = mstack.pop()
            res += arr[ind] * (ind+1) * (len(arr)-ind)
        
        return res%mod
