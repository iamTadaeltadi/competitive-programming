class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        c=0
        x=[]
        g=0
        for i in nums:
            if target==i:
                g+=1
            elif target>i:
                c+=1
            else:pass
        y=c
        for j in range(g):
            x.append(y)
            y+=1
            
        return x
        
