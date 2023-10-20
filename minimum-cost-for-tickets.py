class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def helper(i, covered):
            if i==len(days):
                return 0
            if days[i]>covered:
                return min(helper(i+1, days[i])+costs[0]
                            ,helper(i+1, days[i]+6)+costs[1]
                            ,helper(i+1, days[i]+29)+costs[2])
            else:
                return helper(i+1, covered)
        return helper(0, -1)