class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        for num in nums:
            arr.append(int(num))
        arr.sort()
        return str(arr[-k])