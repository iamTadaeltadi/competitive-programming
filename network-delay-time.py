class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        graph = []



        distance = [float("inf")]*n
        distance[k-1] = 0
        

        for src,dst,signal in (times):
            graph.append([src,dst,signal])
        

        for i in range(n-1):
            for src,dst,signal in graph:
                if distance[src-1] != float("inf") and distance[src-1]+signal < distance[dst-1]:
                    distance[dst-1]= distance[src-1] + signal


        

        for i in distance:
            if i ==float("inf"):
                return -1

        return max(distance)