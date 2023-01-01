class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        x={str(v):i for i,v in enumerate(order)}
        for i in range(len(words)-1):
            maxx=0
            if len(words[i])>len(words[i+1]):
                maxx=words[i+1]
            else:
                maxx=words[i]
            c=0
            ver=True
            while c <len(maxx):
                if  x[words[i][c]] >x[words[i+1][c]]:
                    return False
                elif x[words[i][c]] <x[words[i+1][c]]:
                    ver=False
                    break
                    
                c+=1
            if len(words[i])>len(words[i+1]) and ver:return False
        return True
               
           