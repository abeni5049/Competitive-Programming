class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: 
            return 0
        queue = [beginWord]
        seen = {beginWord}
        num_of_words = 2
        while queue:
            temp = []
            for word in queue:
                for i in range(len(word)):
                    for j in range(26):
                        next_word = word[:i] + chr(ord('a')+j) + word[i+1:]
                        if next_word == endWord:
                            return num_of_words
                        if next_word not in seen and next_word in wordList:
                            temp.append(next_word)
                            seen.add(next_word)
            queue = temp
            num_of_words += 1
        return 0
             
