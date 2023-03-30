class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR=x^y
        count=0
        while XOR>0:
            count+=XOR&1
            XOR>>=1
        return count