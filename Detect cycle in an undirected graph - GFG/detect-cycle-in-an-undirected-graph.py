from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = set()
	    graph=defaultdict(list)
        parent = defaultdict(lambda: None)
        index=0
        for node in adj:
            
            for neg in node:
                graph[index].append(neg)
            index+=1
                
        
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
                    if dfs(neighbor):
                        return True
                elif neighbor != parent[node]:
                    return True
            return False
        
        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False
    		
    		
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends