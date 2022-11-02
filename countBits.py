class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0]
        for num in range(1,n+1):
            count.append(count[num//2] if  num % 2 == 0 else count[num-1]+1 )
        return count
