class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def sym(row,k):
            if row==0 and k==1:
                return 0
            parent=sym(row-1,k//2+k%2)
            if parent ==0:
                if k%2:
                    return 0
                else:
                    return 1
            else:
                if k%2:
                    return 1
                else:
                    return 0
                
            
        
        return sym(n,k)
    