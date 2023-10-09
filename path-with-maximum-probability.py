class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        



        graph = defaultdict(list)

        for edge in range(len(edges)):
            graph[edges[edge][0]].append([edges[edge][1],succProb[edge]])
            graph[edges[edge][1]].append([edges[edge][0],succProb[edge]])


        

        heap = [(-1,start_node)]
        seen =set()
        while heap:
            weight,node = heapq.heappop(heap)
            if node ==end_node:
                return -weight

            if node in seen:
                continue

            
            seen.add(node)

            for neg,newWeight in graph[node]:
                if neg not in seen:
                    heapq.heappush(heap,(weight*newWeight,neg))



        
        return float(0)