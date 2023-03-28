class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        stack=[source]
        visited=set()
        while len(stack)>0:
            curr=stack.pop()
            if curr==destination:
                return True
            
            for i in graph[curr]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
                    
        return False
            
            