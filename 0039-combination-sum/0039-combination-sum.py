class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def combSum(curr,index):
            if sum(curr)==target:
                res.append(curr.copy())
                return 
            if sum(curr)>target or index >=len(candidates):
                return 
            curr.append(candidates[index])
            combSum(curr,index)
            curr.pop()
            combSum(curr,index+1)
            
            return None
            
        combSum([],0)
        return res