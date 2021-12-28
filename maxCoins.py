class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if len(piles) == 3:
            return piles[1]
        result = count = 0
        for i in range(2,len(piles),2):
            if( len(piles)//3 == count):
                break
            result += piles[-i]
            count +=1     
        return result
            