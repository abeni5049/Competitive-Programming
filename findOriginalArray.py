class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        freq = Counter(changed)
        changed.sort()
        original = []
        for num in changed:
            if num == 0 and freq[num] >1:
                freq[num] -= 2
                original.append(num)
            elif num != 0 and freq[num] and freq[num*2]:
                freq[num] -= 1
                freq[num*2] -= 1
                original.append(num)
        return original if len(original) == len(changed)//2 else []
              
                
