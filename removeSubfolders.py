class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Solution:
    def __init__(self):
        self.root = Trie()
    def addWord(self,word):
        curr = self.root
        word = word.split('/')
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.isEnd = True
    def isPre(self,word):
        curr = self.root
        word = word.split('/')
        for char in word:
            if char not in curr.children:return False
            curr = curr.children[char]
            if curr.isEnd:return True
        return curr.isEnd
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for fol in folder:
            if not res or (res and not self.isPre(fol)):
                self.addWord(fol)
                res.append(fol)
        return res
                
