class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        queue=[source]
        visited=set()
        while queue:
            curr=queue.pop(0)
            if curr==destination:
                return True
            
            for i in graph[curr]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                    
        return False
            
            