class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        max_ = 0
        l = r = 0
        while r < len(fruits):
            if fruits[r] in freq:
                freq[fruits[r]] += 1
            else:
                freq[fruits[r]] = 1
            if len(freq) <= 2:
                max_ = max(max_,r-l+1)
                r += 1
            else:
                if len(freq) > 2:
                    freq[fruits[l]] -= 1
                    if freq[fruits[l]] == 0: del freq[fruits[l]]
                    l += 1
                    r += 1
        return max_
