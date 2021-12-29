class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(a,k):
            for i in range(k//2):
                a[i],a[k-i-1]=a[k-i-1],a[i]
                
        result = []
        n = len(arr)
        for i in range(n):
            maxIndex = arr.index(n-i)
            if maxIndex != len(arr)-i-1:
                if maxIndex != 0:
                    flip(arr,maxIndex+1)
                    result.append(maxIndex+1)
                flip(arr,n-i)
                result.append(n-i)
        return result

            
        
