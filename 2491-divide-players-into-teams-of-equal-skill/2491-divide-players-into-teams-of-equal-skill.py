class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        
        [1,2,3,3,4,5]
        
        """
        d=defaultdict(int)
        target=min(skill)+max(skill)
        tot =0
        count=0
        for i in skill:
            j=target-i
            if d[j] ==0:
                d[i]+=1
            else:
                count+=2
                d[j]-=1
                tot+=i*j
        if count==len(skill):
            return tot
        return -1
                

                
        
        
            
            
            
                
        
        