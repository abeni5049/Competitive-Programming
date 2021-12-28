class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = list(Counter(arr).values())
        frequency.sort(reverse=True)
        result  = 1
        freq = frequency[0]
        for i in range(len(arr)-1):
            if freq >= len(arr)//2:
                return result
            else:
                result += 1
                freq += frequency[i+1]