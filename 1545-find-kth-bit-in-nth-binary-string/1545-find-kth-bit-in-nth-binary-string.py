class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res='0'
        def binary(nth):
            nonlocal res
            if nth==n:
                return res
            inverted=list(res)
            for i in range(len(inverted)):
                if inverted[i]=="0":
                    inverted[i]="1"
                else:
                    inverted[i]="0"
            res+="1"+"".join(inverted[::-1])
            binary(nth+1)
        binary(1)
        return res[k-1]
            