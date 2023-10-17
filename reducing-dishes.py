class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()


        @cache
        def dp(index,ind):

            if index == len(satisfaction):
                # print(tot)
                return 0
            

            return max((satisfaction[index] * ind +dp(index+1,ind+1)),dp(index+1,ind))

        return dp(0,1)