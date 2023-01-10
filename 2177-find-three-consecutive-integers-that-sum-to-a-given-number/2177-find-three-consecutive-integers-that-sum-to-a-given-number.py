class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x=((num-3)/3.0)
        if x==int(x):
            return [int(x),int(x+1),int(x+2)]
        return []