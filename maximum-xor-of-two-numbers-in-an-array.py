class Trie:

    def init(self, max_bit_len):
        self.root = TrieNode()
        self.max_bit_len = max_bit_len
    
    def insert(self, num):
        ptr = self.root
        xor_node = self.root

        for j in range(self.max_bit_len, -1, -1):
            i = (num>>j)&1
            if i == 0:
                if ptr.zero is None:
                    ptr.zero= TrieNode()
                ptr = ptr.zero
            else:
                if ptr.one is None:
                    ptr.one = TrieNode()
                ptr = ptr.one

            if i == 0:
                if xor_node.one is not None:
                    xor_node = xor_node.one
                else:
                    xor_node = xor_node.zero
            else:
                if xor_node.zero is not None:
                    xor_node = xor_node.zero
                else:
                    xor_node = xor_node.one
           
        ptr.val = num
        return xor_node.val

    def findCompliment(self, num):
        ptr = self.root
        for j in range(self.max_bit_len, -1, -1):
            i = (num>>j)&1
            

        return ptr.val



class TrieNode:
    def init(self):
        self.zero = None
        self.one = None
        self.val = -1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        max_bit_len = 0
        for n in nums:
            max_bit_len =  max(n.bit_length(), max_bit_len)

        # trie = Trie(max_bit_len)
        # # for num in nums:
        # #     trie.insert(num)
        # max_xor = 0

        # for num in nums:
        #     max_xor = max(max_xor, num ^ trie.insert(num))
        # return max_xor

        trie = {}
        
        max_xor = 0

        for num in nums:
            cur_xor = 0
            cur_node = trie
            xor_node = trie
            for j in range(max_bit_len, -1, -1):
                bit = num >> j & 1

                if bit not in cur_node:
                    cur_node[bit] = {}
                cur_node = cur_node[bit]
                if 1 - bit in xor_node:
                    cur_xor = cur_xor | (1 << j)
                    xor_node = xor_node[1-bit]
                else:
                    xor_node = xor_node[bit]

            print(num, cur_node)
            max_xor = max(cur_xor, max_xor)

        return max_xor