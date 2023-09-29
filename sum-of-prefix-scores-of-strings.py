class Trie():
    def __init__(self):
        self.children = {}
        self.score = 0


class Solution:
    def __init__(self):
        self.root = Trie()
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []

        for w in words:
            self.insert(w)

        for w in words:
             ans.append(self.getScore(w))
        return ans
    


    def insert(self,word):
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
                
            curr = curr.children[i]
            curr.score+=1
    def getScore(self,prefix):
        totScore = 0
        curr = self.root

        for i in prefix:
            if i not in curr.children:
                curr.children[i] = Trie()
                
            curr = curr.children[i]
            totScore+= curr.score
        return totScore