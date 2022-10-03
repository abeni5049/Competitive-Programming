class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fruit = {}
        for pos,num in fruits:
            fruit[pos] = num
            
        sum_ = [0]
        for i in range(fruits[-1][0]+1):
            sum_.append(sum_[-1]+fruit.get(i,0))
        
        res = 0
        for pos,num in fruits:
            r = min(max(2*pos+k-startPos,startPos),len(sum_)-2)
            l = max(min(2*pos-k-startPos,startPos),0)
            if abs(pos-startPos) <= k:
                if pos <= startPos: 
                    res = max(res,sum_[r+1]-sum_[pos])
                elif pos > startPos:
                    res = max(res,sum_[pos+1]-sum_[l])
        return res
