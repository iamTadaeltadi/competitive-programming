class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.helper(n,k)+1

    def helper(self, n:int, k:int)-> int:
        if(n==1):
            return 0
        prevWinner = self.helper(n-1, k)
        return (prevWinner + k) % n