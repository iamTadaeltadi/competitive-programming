from collections import defaultdict
import math
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(bombs)):
            radius = bombs[i][2]
            x, y = bombs[i][0], bombs[i][1]  
            for j in range(len(bombs)):
                if i != j:
                    eculidian_distance = math.pow((x - bombs[j][0])**2 + (y - bombs[j][1])**2, 1/2)  # Incorrect power usage
                
                    if eculidian_distance <= radius:
                        graph[i].append(j)
        
        count = 1

        for i in range(len(bombs)):
            stack = [i]
            visited = set()
            c = 1
            while stack:
                curr = stack.pop()
                visited.add(curr)
                for neg in graph[curr]:
                    if neg not in visited:
                    stack.append(neg) 
                    c += 1 
                
            count = max(count, len(visited))
        return count
