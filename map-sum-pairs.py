class Trie():
    def __init__(self):
        self.children = dict()
        self.sum = 0
        self.original_val = 0


class MapSum:

    def __init__(self):
        self.root = Trie()

    def isWordExistesBefore(self,word):
        curr = self.root

        for i in word:
            if i not in curr.children:
                return 0
            curr = curr.children[i]
        

        
        return curr.original_val






    def insert(self, key: str, val: int) -> None:
        curr = self.root

        sum_val= self.isWordExistesBefore(key)

        if sum_val==0:

            for i in key:
                if i not in curr.children:
                    curr.children[i] = Trie()
                curr = curr.children[i]
                curr.sum+=val
            
        else:
            for i in key:
                if i not in curr.children:
                    curr.children[i] = Trie()
                curr = curr.children[i]
                curr.sum += (val-sum_val) 
        curr.original_val = val
        

        

    def sum(self, prefix: str) -> int:
        curr = self.root

        for i in prefix:
            if i not in curr.children:
                return 0
            curr = curr.children[i]
            
        return curr.sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)