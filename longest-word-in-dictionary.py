class Trie():
    def __init__(self):
        self.children ={}
        self.is_end =False


class Solution:
    def __init__(self):
        self.root =Trie()

    def longestWord(self, words: List[str]) -> str:

        for word in words:
            self.insert(word)
        
        ans = ''
        

        for i in words:
            curr =self.canBeBuilt(i)
            if len(ans) <len(curr):
                ans = curr
            elif len(ans) == len(curr):
                if ans>curr:
                    ans =curr
        return ans 


        
    

    def insert(self,word):
        curr =self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
            curr =curr.children[i]

        curr.is_end =True

    def canBeBuilt(self,word):
        curr =self.root

        for i in word:
            curr =curr.children[i]
            if not  curr.is_end:
                return ""
            

        return word