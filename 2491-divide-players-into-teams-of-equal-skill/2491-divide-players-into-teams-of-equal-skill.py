class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        
        [1,2,3,3,4,5]
        
        """
        skill.sort()
        l=0
        r=len(skill)-1
        pair=skill[l] +skill[r]
        tot=0
        while l<r:
            if pair !=skill[l]+skill[r]:
                return -1
            tot+=skill[l]*skill[r]
            l+=1
            r-=1
        return tot
            
            
            
                
        
        