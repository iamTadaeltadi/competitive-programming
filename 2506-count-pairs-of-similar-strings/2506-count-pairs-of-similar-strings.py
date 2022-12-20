class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1 , len(words)):
                if set(words[i]) == set(words[j]):
                    count +=1
        return count 
        