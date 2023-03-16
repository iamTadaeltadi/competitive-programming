class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        def combine(index,curr):
            if len(curr) == k:
                res.append([i for i in curr])
                return 
            if index > n:
                return
            
            for i in range(index,n+1):
                curr.append(i)
                combine(i+1,curr)
                curr.pop()
                
        combine(1,[])
        return res
            
                
            