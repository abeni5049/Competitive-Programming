class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = []
        for i in range(len(nums)):
            s.append(str(nums[i]))
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] + s[j] > s[j] + s[i]:
                    s[i],s[j] = s[j],s[i]
        largestNum = ""
        for i in s:
            largestNum += i
        if largestNum[0] == "0":
            return "0"
        return largestNum