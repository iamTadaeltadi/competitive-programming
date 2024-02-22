class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]*n
        outdegree = [0]*n

        graph =defaultdict(int)
        for i in range(len(trust)):
            graph[trust[i][0]] = trust[i][1]
            indegree[trust[i][1]-1]+=1
            outdegree[trust[i][0]-1]+=1

        
        

        degree = list(zip(indegree,outdegree))
        print(degree)
        

        for i in range(len(degree)):
            if degree[i][0]==n-1 and degree[i][1]==0:
                return i+1
        return -1