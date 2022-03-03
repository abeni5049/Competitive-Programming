class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        revPrefix = [nums[len(nums)-1]]
        for i in range(len(nums)-2,-1,-1):
            revPrefix.append(revPrefix[-1]*nums[i])
            
        prefix = [nums[0]]
        res = [revPrefix[-2]]
        for j in range(1,len(nums)-1):
            prefix.append(prefix[-1]*nums[j])
            res.append(prefix[j-1]*revPrefix[-j-2])    
        res.append(prefix[len(nums)-2])
        return res
