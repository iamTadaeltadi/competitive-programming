class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        x=s.split()
        maxx=0
        for i in x:
            maxx=max(len(i),maxx)
        listt=[]
        for i in range(maxx):
            v=[]
            for j in range(len(x)):
                if i <len(x[j]):
                    v.append(x[j][i])
                    
                else:
                    v.append(" ")
            strr=''.join(v).rstrip()
            listt.append(strr)
        return listt
            
            