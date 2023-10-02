class Solution:
    def __init__(self):
        self.d={}
    def tribonacci(self, n: int) -> int:

        if n in self.d:
            return  self.d[n]

        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        self.d[n]=self.tribonacci(n-1) + self.tribonacci(n-2) +self.tribonacci(n-3)

        return self.d[n]