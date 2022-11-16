class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        s = sorted(count.keys(),key=lambda x: count[x], reverse=True)
        last = count[s[0]]
        min_deletions = 0
        for i in range(1,len(s)):
            if last <= count[s[i]]:
                last -= 1
                if last < 0:
                    last = 0
                min_deletions += count[s[i]] - last
            else:
                last = count[s[i]]
        return min_deletions
                
          
            
               
