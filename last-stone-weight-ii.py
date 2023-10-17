class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        @cache
        def dp(index,res):

            if index ==len(stones):
                return res if res>=0 else float("inf")


            return min(dp(index+1,res-stones[index]),dp(index+1,res+stones[index]))
        
        return dp(0,0)