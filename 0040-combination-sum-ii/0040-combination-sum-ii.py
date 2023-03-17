class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def combinate(curr,index):
            
            if sum(curr)==target:
                
                res.append((curr[:]))
                return
            
            for i in range(index,len(candidates)):
                if i-1 >= index and candidates[i-1] ==candidates[i]:
                    continue
                if sum(curr)+candidates[i]>target:
                    return 
                curr.append(candidates[i])
                combinate(curr,i+1)
                curr.pop()
                
                
        combinate([],0)
        return res
