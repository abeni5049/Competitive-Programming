class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9+7
        res = 0
        mstack = []
        for i,num in enumerate(arr):
            while mstack and arr[mstack[-1]] >= num:
                ind = mstack.pop()
                left = mstack[-1] if mstack else -1
                res += arr[ind] * (i-ind) * (ind-left)
            mstack.append(i)
        
        while mstack:
            ind = mstack.pop()
            left = mstack[-1] if mstack else -1
            res += arr[ind] * (len(arr)-ind) * (ind-left)
            
        return res%mod
