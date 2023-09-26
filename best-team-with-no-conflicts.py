class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        d =defaultdict(list)


        x= list(zip(ages,scores))
        x.sort()

        dp = [x[i][1] for i in range(len(x))]
        print(x)

        for i in range(len(x)-1,-1,-1):
            for j in range(i+1,len(x)):

                if  x[i][1] <=x[j][1]:
                    dp[i]=max(dp[j]+x[i][1],dp[i])
        return max(dp)