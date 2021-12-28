class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        frequency = dict(sorted(frequency.items(),key=lambda x:x[1],reverse=True))
        result = []
        count = 0
        for i in frequency:
            if count == k:
                break
            result.append(i)
            count += 1
        return result