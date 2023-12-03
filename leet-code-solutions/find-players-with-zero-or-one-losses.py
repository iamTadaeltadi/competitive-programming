class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        d=defaultdict(int)
        ans1=set()
        ans2=set()
        for i,j in matches:
            d[j]+=1
        for i,j in matches:
            if i not in d:
                ans1.add(i)
        for i in d:
            if d[i]==1:
                ans2.add(i)
        x=(list(ans1))
        y=list(ans2)
        x.sort()
        y.sort()
        return [x,y]