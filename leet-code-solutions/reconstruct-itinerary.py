from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        allCity = set()

        for src, dsc in tickets:
            graph[src].append(dsc)
            allCity.add(src)
            allCity.add(dsc)

        for city in graph:
            graph[city].sort()
            
            
        def dfs(curr, path):
            if len(path) == len(tickets)+1:
                return path

            for neg in graph[curr][:]:  # Create a copy of the list before modifying
                graph[curr].remove(neg)
                x = dfs(neg, path + [neg])
                graph[curr].append(neg)
                
                if x:  # If a valid path is found, return it
                    return x
            
            return []

        return dfs("JFK", ["JFK"])







        