class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0
        index = 0
        for i,char in enumerate(chars):
            if i == len(chars)-1 or chars[i] != chars[i+1]:
                chars[index] = chars[i]
                index += 1
                if i>pos:
                    count = i - pos + 1
                    for num in str(count):
                        chars[index] = num
                        index += 1
                pos = i + 1
        return index
