class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        d={}
        for i in range(len(words)):
            d[str(set(words[i]))]=1+d.get(str(set(words[i])),0)
        for i in d.values():
            if i>=2:
                count+=((i-1)*(i))/2
        return count

        
            
            
             