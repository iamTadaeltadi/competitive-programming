class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.count += 1

    def common_str(self, word, n):
        curr = self.root
        ans = ''

        for char in word:
            
            curr = curr.children[char]
            if curr.count == n:
                ans += char
        return ans

class Solution:
    def longestCommonPrefix(self, v):
        trie = Trie()

        for word in v:
            trie.insert(word)
        
        n = len(v)
        v.sort()
        return trie.common_str(v[0], n)
