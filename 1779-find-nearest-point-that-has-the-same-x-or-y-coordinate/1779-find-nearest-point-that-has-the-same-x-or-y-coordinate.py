class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        dic=defaultdict(list)
        index=0
        for i,j in points:
            if i==x or j==y:
                manhattan=abs(i-x)+abs(j-y)
                dic[manhattan].append(index)
            index+=1
        if not dic:
            return -1
        minn=min(dic.keys())
        return dic[minn][0]
    
    