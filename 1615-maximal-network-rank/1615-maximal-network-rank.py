class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        largest=0
        for i in roads:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        for i in range(n):
            for j in range(i+1,n):
                rank=len(graph[i])+len(graph[j]) +(-1 if j in graph[i] else 0)
                largest=max(rank,largest)
        return largest