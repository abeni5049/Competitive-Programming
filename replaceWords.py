class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def __init__(self):
        self.root = Trie()
    def addWord(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.isEnd = True
    def isPre(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isEnd
        
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        for word in dictionary:
            self.addWord(word)
        for i,word in enumerate(words):
            for j in range(len(word)):
                if self.isPre(word[:j+1]):
                    words[i] = word[:j+1]
                    break
        s = ''
        for i,word in enumerate(words):
            s += word
            if i != len(words)-1: s += ' '
        return s
        
