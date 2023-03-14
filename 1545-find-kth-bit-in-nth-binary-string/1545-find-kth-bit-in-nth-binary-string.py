class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def binary(nth):
            
            if nth==1:
                return "0"
            s=binary(nth-1)
            inverted=list(s)
            for i in range(len(inverted)):
                if inverted[i]=="0":
                    inverted[i]="1"
                else:
                    inverted[i]="0"
            res= s+ "1"+"".join(inverted[::-1])
            return res
            
        
        return binary(n)[k-1]
            