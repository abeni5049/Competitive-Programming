class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r, count, res = 0, 0, 0, len(blocks)
        while r < len(blocks):
            if blocks[r] == 'W':
                count += 1
            if r-l+1 == k:
                res = min(res,count)
                if blocks[l] == 'W':
                    count -= 1
                l += 1
            r += 1
        return res
                
