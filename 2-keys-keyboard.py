from functools import lru_cache

class Solution:
    def minSteps(self, n: int) -> int:
        ans = float("inf")
        catch = {}
        if n == 1:
            return 0

        def dp(op,total, last_op):

            if total >n:
                return float('inf')
            
            if total == n:
                return 0

            if (op,total, last_op) in catch:
                return catch[(op,total, last_op)]


            if op=="C":
                 catch[(op,total, last_op)]=1+dp("P",total+last_op,last_op)
            else:
                catch[(op,total, last_op)] = min(1+dp("C",total,total),1+dp("P",total+last_op,last_op))
            return catch[(op,total, last_op)]
            

           

            
            

        return 1+ dp("C", 1,1)

# Example usage
solution = Solution()
print(solution.minSteps(9))