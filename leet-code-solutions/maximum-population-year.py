class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0]*2051

        for i,j in logs:
            prefix[i]+=1
            prefix[j]-=1
        

        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        

        
        

        

        return prefix.index(max(prefix))


