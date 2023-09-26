class TrieNode:
    def __init__(self):
        self.is_end =False
        self.children = [None for i in range(26)]


class WordDictionary:

    def __init__(self):
        self.root =TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if not curr.children[ord(c)-97]:
                curr.children[ord(c)-97]=TrieNode()
            curr = curr.children[ord(c)-97]
        
        curr.is_end =True
        # print(curr.is_end,word[])
        
        

    def search(self, word: str) -> bool:


        def dfs(i,node):
            

            if i>=len(word):
                return node.is_end

            if i>=len(word):
                return False
            if word[i]==".":
                temp = False
                # print(node.children)
                for w in node.children:
                    if w:
                         temp = temp or dfs(i+1,w)
                return temp


            if node.children[ord(word[i])-97]:
                return dfs(i+1,node.children[ord(word[i])-97])
        return dfs(0,self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)